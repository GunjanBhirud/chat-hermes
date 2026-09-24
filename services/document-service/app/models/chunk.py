from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
import datetime
from ..config import settings
from ..db.session import Base

class DocumentChunk(Base):
    __tablename__ = "document_chunks"
    id = Column(UUID(as_uuid=True), primary_key=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"), nullable=False)
    owner_id = Column(UUID(as_uuid=True), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(settings.embedding_dimensions))
    page_start = Column(Integer, nullable=True)
    page_end = Column(Integer, nullable=True)
    heading_path_text = Column(String, nullable=True)
    source_metadata_text = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

    document = relationship("Document", back_populates="chunks")
