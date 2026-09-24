from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class ParsedSection:
    text: str
    page: int
    metadata: Dict[str, Any]

class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> List[ParsedSection]:
        pass
