import uuid
import json
from typing import AsyncGenerator
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sse_starlette.sse import EventSourceResponse
from ..schemas.chat import MessageCreate, MessageResponse
from ..models.conversation import Conversation
from ..models.message import Message
from ..db.session import get_db
from ..llm.openai_compatible import get_llm_provider
from ..clients.document_service import retrieve_chunks
from ..prompts.document_qa import SYSTEM_PROMPT_TEMPLATE, build_context_string

router = APIRouter(prefix="/api/v1/conversations/{conversation_id}/messages", tags=["messages"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Security(security)) -> uuid.UUID:
    try:
        return uuid.UUID(credentials.credentials)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("")
async def create_message(
    conversation_id: uuid.UUID,
    payload: MessageCreate,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    conv = await db.scalar(select(Conversation).where(Conversation.id == conversation_id, Conversation.owner_id == user_id))
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
        
    doc_ids = conv.document_ids or []
    
    # Save user message
    user_msg = Message(id=uuid.uuid4(), conversation_id=conversation_id, role="user", content=payload.content)
    db.add(user_msg)
    await db.commit()
    
    provider = get_llm_provider()
    
    # Embed question
    try:
        query_embedding = await provider.embed(payload.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Retrieve chunks
    try:
        chunks = await retrieve_chunks(doc_ids, query_embedding, top_k=5)
    except Exception as e:
        # Fallback to no chunks instead of crashing the whole chat if retrieval times out
        chunks = []
    chunk_ids = [uuid.UUID(c["chunk_id"]) for c in chunks]
    
    context_str = build_context_string(chunks)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context_str)
    
    async def event_generator() -> AsyncGenerator[dict, None]:
        # Track output
        full_response = []
        try:
            async for token in provider.generate_stream(system_prompt, payload.content):
                full_response.append(token)
                yield {"event": "token", "data": json.dumps({"text": token})}
                
            for i, c in enumerate(chunks):
                yield {"event": "source", "data": json.dumps({"source_id": f"S{i+1}", "chunk_id": c["chunk_id"]})}
                
            assistant_msg = Message(id=uuid.uuid4(), conversation_id=conversation_id, role="assistant", content="".join(full_response), source_chunk_ids=chunk_ids)
            db.add(assistant_msg)
            await db.commit()
            
            yield {"event": "message_complete", "data": json.dumps({"message_id": str(assistant_msg.id)})}
        except Exception as e:
            yield {"event": "error", "data": json.dumps({"message": str(e)})}
            
    return EventSourceResponse(event_generator())
