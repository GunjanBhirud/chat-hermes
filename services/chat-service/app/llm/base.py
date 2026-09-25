from abc import ABC, abstractmethod
from typing import List, AsyncGenerator

class LLMProvider(ABC):
    @abstractmethod
    async def embed(self, text: str) -> List[float]:
        pass
        
    @abstractmethod
    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        pass
