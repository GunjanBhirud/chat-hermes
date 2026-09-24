from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ..parsers.base import ParsedSection
from ..config import settings

def chunk_sections(sections: List[ParsedSection]) -> List[ParsedSection]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )
    
    chunks = []
    for section in sections:
        split_texts = splitter.split_text(section.text)
        for text_chunk in split_texts:
            chunks.append(ParsedSection(
                text=text_chunk,
                page=section.page,
                metadata=section.metadata
            ))
            
    return chunks