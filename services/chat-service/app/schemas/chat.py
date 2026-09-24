import uuid
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ConversationCreate(BaseModel):
    document_ids: List[uuid.UUID]
    title: Optional[str] = "New Conversation"

class ConversationResponse(BaseModel):
    conversation_id: uuid.UUID
    title: str
    document_ids: List[uuid.UUID]
    
    model_config = ConfigDict(from_attributes=True)

class MessageCreate(BaseModel):
    content: str

class MessageResponse(BaseModel):
    id: uuid.UUID
    role: str
    content: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
