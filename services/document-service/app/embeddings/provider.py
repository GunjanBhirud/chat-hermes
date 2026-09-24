from abc import ABC, abstractmethod
from typing import List
import httpx
from ..config import settings

class EmbeddingProvider(ABC):
    @abstractmethod
    async def embed_text(self, text: str) -> List[float]:
        pass

class OpenAICompatibleProvider(EmbeddingProvider):
    def __init__(self):
        self.base_url = settings.embedding_base_url
        self.model = settings.embedding_model
        self.api_key = settings.embedding_api_key
        
    async def embed_text(self, text: str) -> List[float]:
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{self.base_url}/embeddings", headers={
                "Authorization": f"Bearer {self.api_key}"
            }, json={
                "model": self.model,
                "input": text
            })
            res.raise_for_status()
            return res.json()["data"][0]["embedding"]

def get_embedding_provider() -> EmbeddingProvider:
    return OpenAICompatibleProvider()
