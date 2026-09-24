import uuid
from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.document import DocumentResponse, DocumentDetailResponse
from ..models.document import Document
from ..db.session import get_db
from ..storage.file_storage import save_upload_file, delete_file
from ..config import settings
from sqlalchemy import select
from ..db.session import AsyncSessionLocal
from ..ingestion.processor import process_document

async def run_pipeline(doc_id: uuid.UUID):
    async with AsyncSessionLocal() as session:
        await process_document(doc_id, session)

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Security(security)) -> uuid.UUID:
    try:
        return uuid.UUID(credentials.credentials)
    except ValueError:
        raise HTTPException(status_code=401, detail={"code": "UNAUTHORIZED", "message": "Invalid token"})

@router.post("", response_model=DocumentResponse, status_code=202)
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail={"code": "INVALID_FILE", "message": "No filename"})
        
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "docx", "md"]:
        raise HTTPException(status_code=400, detail={"code": "INVALID_FILE_TYPE", "message": "Unsupported file."})
        
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    
    if size > settings.max_file_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail={"code": "FILE_TOO_LARGE", "message": f"Max {settings.max_file_size_mb}MB"})
        
    doc_id = uuid.uuid4()
    storage_key = save_upload_file(file, doc_id)
    
    new_doc = Document(
        id=doc_id,
        owner_id=user_id,
        name=file.filename,
        original_filename=file.filename,
        mime_type=file.content_type or "application/octet-stream",
        file_size=size,
        storage_key=storage_key,
        status="QUEUED"
    )
    
    db.add(new_doc)
    await db.commit()
    
    background_tasks.add_task(run_pipeline, doc_id)
    
    return DocumentResponse(document_id=doc_id, name=new_doc.name, status=new_doc.status)

@router.get("", response_model=List[DocumentResponse])
async def list_documents(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).where(Document.owner_id == user_id))
    docs = result.scalars().all()
    return [DocumentResponse(document_id=d.id, name=d.name, status=d.status) for d in docs]

@router.get("/{document_id}", response_model=DocumentDetailResponse)
async def get_document(document_id: uuid.UUID, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    doc = await db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user_id))
    if not doc:
        raise HTTPException(status_code=404, detail={"code": "DOCUMENT_NOT_FOUND", "message": "Not found"})
        
    return DocumentDetailResponse(
        id=doc.id,
        owner_id=doc.owner_id,
        name=doc.name,
        type=doc.mime_type,
        size_bytes=doc.file_size,
        status=doc.status,
        page_count=doc.page_count,
        chunk_count=doc.chunk_count,
        created_at=doc.created_at,
        processed_at=doc.processed_at
    )
    
@router.delete("/{document_id}", status_code=204)
async def delete_document(document_id: uuid.UUID, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    doc = await db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user_id))
    if not doc:
        raise HTTPException(status_code=404, detail={"code": "DOCUMENT_NOT_FOUND", "message": "Not found"})
        
    delete_file(doc.storage_key)
    await db.delete(doc)
    await db.commit()
    return
