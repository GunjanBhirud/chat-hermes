import httpx
import uuid
from typing import List, Dict, Any
from ..config import settings

async def retrieve_chunks(document_ids: List[uuid.UUID], query_embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
    # Internal retrieval
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{settings.document_service_url}/internal/retrieval/search",
            json={
                "document_ids": [str(x) for x in document_ids],
                "query_embedding": query_embedding,
                "top_k": top_k
            }
        )
        if res.status_code == 200:
            return res.json().get("results", [])
        return []
