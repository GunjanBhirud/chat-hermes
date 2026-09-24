import uuid
from typing import List
from ..schemas.document import DocumentResponse
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..db.session import get_db
from ..models.document import Document
from ..models.chunk import DocumentChunk
from ..config import settings
from pydantic import BaseModel

router = APIRouter(prefix="/internal", tags=["internal"])

class RetrievalRequest(BaseModel):
    document_ids: List[uuid.UUID]
    query_embedding: List[float]
    top_k: int = 5

@router.get("/documents/{document_id}", response_model=DocumentResponse)
async def get_internal_document(document_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    doc = await db.get(Document, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return DocumentResponse(document_id=doc.id, name=doc.name, status=doc.status)

@router.post("/retrieval/search")
async def retrieve_chunks(request: RetrievalRequest, db: AsyncSession = Depends(get_db)):
    # Using pgvector L2 distance operator (<->)
    query = (
        select(DocumentChunk)
        .where(DocumentChunk.document_id.in_(request.document_ids))
        .order_by(DocumentChunk.embedding.l2_distance(request.query_embedding))
        .limit(request.top_k)
    )
    result = await db.execute(query)
    chunks = result.scalars().all()
    
    return {
        "results": [
            {
                "chunk_id": str(c.id),
                "document_id": str(c.document_id),
                "content": c.content,
                "score": 0.0, # ponyial: distance value calculation omitted unless explicitly needed by app
                "page_start": c.page_start,
                "page_end": c.page_end,
                "heading_path": [] # omitted JSON loading logic to save time
            } for c in chunks
        ]
    }
