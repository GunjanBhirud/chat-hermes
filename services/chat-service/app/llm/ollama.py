from abc import ABC, abstractmethod
from typing import List, AsyncGenerator
import httpx
from ..config import settings

class LLMProvider(ABC):
    @abstractmethod
    async def embed(self, text: str) -> List[float]:
        pass
        
    @abstractmethod
    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        pass

class OllamaLLMProvider(LLMProvider):
    def __init__(self):
        self.base_url = settings.llm_base_url
        self.model = settings.llm_model
        
    async def embed(self, text: str) -> List[float]:
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{self.base_url}/api/embeddings", json={
                "model": "mxbai-embed-large", # Matching documents embedding assumption ideally
                "prompt": text
            })
            return res.json()["embedding"]

    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        async with httpx.AsyncClient(timeout=120) as client:
            async with client.stream("POST", f"{self.base_url}/api/generate", json={
                "model": self.model,
                "system": system_prompt,
                "prompt": user_prompt,
                "stream": True
            }) as response:
                async for line in response.aiter_lines():
                    if line:
                        import json
                        data = json.loads(line)
                        if "response" in data:
                            yield data["response"]

def get_llm_provider() -> LLMProvider:
    return OllamaLLMProvider()
