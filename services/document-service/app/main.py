from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks, Security
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uuid
import os
from .config import settings
from .db.session import engine, Base
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Document Service")
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    # MVP: Using token blindly as user_id to simulate external gateway auth.
    return credentials.credentials

from .api.documents import router as documents_router
from .api.internal import router as internal_router
app.include_router(documents_router)
app.include_router(internal_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/v1/documents", status_code=202)
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user_id: str = Security(get_current_user_id)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail={"code": "INVALID_FILE", "message": "No filename"})
    
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    
    if size > settings.max_file_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail={"code": "FILE_TOO_LARGE", "message": f"Max {settings.max_file_size_mb}MB"})
        
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "docx", "md"]:
        raise HTTPException(status_code=400, detail={"code": "INVALID_FILE_TYPE", "message": "Unsupported file API"})
        
    doc_id = str(uuid.uuid4())
    storage_key = f"{doc_id}_{ext}"
    storage_path = os.path.join(settings.storage_path, storage_key)
    
    with open(storage_path, "wb") as f:
        f.write(file.file.read())
        
    # TODO: Write QUEUED state to DB
    
    return {"document_id": doc_id, "name": file.filename, "status": "QUEUED"}
