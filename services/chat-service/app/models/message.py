from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
import datetime
from ..db.session import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False) # 'user' or 'assistant'
    content = Column(String, nullable=False)
    source_chunk_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=True) # Inline relation substitute for sources
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")
