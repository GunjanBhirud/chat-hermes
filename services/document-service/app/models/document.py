from sqlalchemy import Column, String, Integer, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import datetime
from ..db.session import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), primary_key=True)
    owner_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    original_filename = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    file_size = Column(BigInteger, nullable=False)
    storage_key = Column(String, nullable=False)
    status = Column(String, nullable=False)
    error_code = Column(String, nullable=True)
    error_message = Column(String, nullable=True)
    page_count = Column(Integer, nullable=True)
    chunk_count = Column(Integer, nullable=True)
    embedding_model = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    processed_at = Column(DateTime(timezone=True), nullable=True)

    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")
