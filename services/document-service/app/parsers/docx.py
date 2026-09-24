import docx
from typing import List
from .base import BaseParser, ParsedSection

class DocxParser(BaseParser):
    def parse(self, file_path: str) -> List[ParsedSection]:
        sections: List[ParsedSection] = []
        try:
            doc = docx.Document(file_path)
            for i, para in enumerate(doc.paragraphs):
                text = para.text
                if text.strip():
                    sections.append(ParsedSection(
                        text=text,
                        page=1, # Pages not distinct in standard docx streaming
                        metadata={"paragraph": i}
                    ))
        except Exception as e:
            raise Exception(f"Failed to parse DOCX: {str(e)}")
        return sections
