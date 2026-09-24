from pydantic import BaseModel, ConfigDict
import uuid
from typing import Optional
from datetime import datetime

class DocumentResponse(BaseModel):
    document_id: uuid.UUID
    name: str
    status: str
    
    model_config = ConfigDict(from_attributes=True)

class DocumentDetailResponse(BaseModel):
    id: uuid.UUID
    owner_id: uuid.UUID
    name: str
    type: str # using mime_type
    size_bytes: int
    status: str
    page_count: Optional[int]
    chunk_count: Optional[int]
    created_at: datetime
    processed_at: Optional[datetime]
    
    model_config = ConfigDict(from_attributes=True)
