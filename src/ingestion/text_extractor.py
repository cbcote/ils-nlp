# src/ingestion/text_extractor.py
from tika import parser

class TextExtractor:
    def extract_text(self, file_path):
        parsed = parser.from_file(file_path)
        return parsed["content"]
