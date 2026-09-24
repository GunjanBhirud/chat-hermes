from abc import ABC, abstractmethod
from typing import List
import httpx
from ..config import settings

class EmbeddingProvider(ABC):
    @abstractmethod
    async def embed_text(self, text: str) -> List[float]:
        pass

class OllamaProvider(EmbeddingProvider):
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.model = settings.embedding_model
        
    async def embed_text(self, text: str) -> List[float]:
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{self.base_url}/api/embeddings", json={
                "model": self.model,
                "prompt": text
            })
            res.raise_for_status()
            return res.json()["embedding"]

def get_embedding_provider() -> EmbeddingProvider:
    # Factory for configuration (could support multiple in future)
    return OllamaProvider()
