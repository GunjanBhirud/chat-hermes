import fitz  # PyMuPDF
from typing import List
from .base import BaseParser, ParsedSection

class PDFParser(BaseParser):
    def parse(self, file_path: str) -> List[ParsedSection]:
        sections: List[ParsedSection] = []
        try:
            with fitz.open(file_path) as doc:
                for i, page in enumerate(doc):
                    text = page.get_text()
                    if text.strip():
                        sections.append(ParsedSection(
                            text=text,
                            page=i + 1,
                            metadata={"page": i + 1}
                        ))
        except Exception as e:
            raise Exception(f"Failed to parse PDF: {str(e)}")
        return sections
