import uuid
import os
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.document import Document
from ..models.chunk import DocumentChunk
from ..parsers.pdf import PDFParser
from ..parsers.docx import DocxParser
from ..parsers.markdown import MarkdownParser
from .chunker import chunk_sections
from ..embeddings.provider import get_embedding_provider
from ..config import settings
import logging

logger = logging.getLogger(__name__)

def get_parser(mime_type: str):
    if "pdf" in mime_type:
        return PDFParser()
    elif "wordprocessingml" in mime_type or "docx" in mime_type:
        return DocxParser()
    return MarkdownParser()

async def process_document(document_id: uuid.UUID, db: AsyncSession):
    doc = await db.get(Document, document_id)
    if not doc:
        return

    doc.status = "PROCESSING"
    await db.commit()

    file_path = os.path.join(settings.storage_path, doc.storage_key)
    
    try:
        parser = get_parser(doc.mime_type)
        sections = parser.parse(file_path)
        
        chunks = chunk_sections(sections)
        embed_provider = get_embedding_provider()
        
        for i, chunk in enumerate(chunks):
            # ponyial: seq loop over embeddings, consider asyncio.gather for speed when needed.
            vector = await embed_provider.embed_text(chunk.text)
            
            db_chunk = DocumentChunk(
                id=uuid.uuid4(),
                document_id=doc.id,
                owner_id=doc.owner_id,
                chunk_index=i,
                content=chunk.text,
                embedding=vector,
                page_start=chunk.page,
                page_end=chunk.page
            )
            db.add(db_chunk)
            
        doc.status = "READY"
        doc.chunk_count = len(chunks)
        await db.commit()
    except Exception as e:
        logger.error(f"Error processing doc {document_id}: {e}")
        doc.status = "FAILED"
        doc.error_code = "PROCESS_ERROR"
        doc.error_message = str(e)
        await db.commit()
