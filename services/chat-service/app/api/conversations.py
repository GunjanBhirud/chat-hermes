import uuid
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..db.session import get_db
from ..models.conversation import Conversation
from ..schemas.chat import ConversationCreate, ConversationResponse

router = APIRouter(prefix="/api/v1/conversations", tags=["conversations"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Security(security)) -> uuid.UUID:
    try:
        return uuid.UUID(credentials.credentials)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("", response_model=ConversationResponse)
async def create_conversation(
    payload: ConversationCreate,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    # TODO: Verify documents access through document_service connector (TC-008 conceptual)
    
    conv_id = uuid.uuid4()
    conv = Conversation(
        id=conv_id,
        owner_id=user_id,
        title=payload.title,
        document_ids=payload.document_ids
    )
    db.add(conv)
    await db.commit()
    return ConversationResponse(
        conversation_id=conv_id,
        title=conv.title,
        document_ids=conv.document_ids
    )

@router.get("/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    conv = await db.scalar(select(Conversation).where(Conversation.id == conversation_id, Conversation.owner_id == user_id))
    if not conv:
        raise HTTPException(status_code=404, detail="Not found")
    return ConversationResponse(
        conversation_id=conv.id,
        title=conv.title,
        document_ids=conv.document_ids
    )
