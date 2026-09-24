from typing import List, AsyncGenerator
import json
import httpx
from ..config import settings
from .base import LLMProvider

class OpenAICompatibleProvider(LLMProvider):
    def __init__(self):
        self.base_url = settings.llm_base_url
        self.model = settings.llm_model
        self.api_key = settings.llm_api_key
        
    async def embed(self, text: str) -> List[float]:
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{self.base_url}/embeddings", headers={
                "Authorization": f"Bearer {self.api_key}"
            }, json={
                "model": settings.embedding_model,
                "input": text
            })
            res.raise_for_status()
            return res.json()["data"][0]["embedding"]

    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        async with httpx.AsyncClient(timeout=120) as client:
            async with client.stream("POST", f"{self.base_url}/chat/completions", headers={
                "Authorization": f"Bearer {self.api_key}"
            }, json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": True
            }) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: ") and line != "data: [DONE]":
                        data = json.loads(line[6:])
                        content = data["choices"][0]["delta"].get("content")
                        if content:
                            yield content

def get_llm_provider() -> LLMProvider:
    return OpenAICompatibleProvider()
