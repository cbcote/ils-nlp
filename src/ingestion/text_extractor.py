from tika import parser

class TextExtractor:
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from a document.
        
        Args:
            file_path: Local path to the document to extract text from (PDF, Word, etc.)
        
        Returns:
            Extracted text from the document
        """
        parsed = parser.from_file(file_path)
        return parsed["content"]
