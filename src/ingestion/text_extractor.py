from tika import parser
import os
import logging

import PyPDF2
import docx2txt
from bs4 import BeautifulSoup

class TextExtractor:
    def __init__(self, config) -> None:
        self.config = config
        tika_server_jar_path = os.path.abspath(config.get('tika_server_jar', 'tika-server.jar'))
        os.environ["TIKA_SERVER_JAR"] = tika_server_jar_path
        self.logger = logging.getLogger(__name__)
    
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from a document.
        
        Args:
            file_path: Local path to the document to extract text from (PDF, Word, etc.)
        
        Returns:
            Extracted text from the document
        """
        self.logger.info(f"Extracting text from file: {file_path}")
        file_extension = os.path.splitext(file_path)[1].lower()
        try:
            if file_extension == '.pdf':
                return self._extract_text_from_pdf(file_path)
            elif file_extension == '.docx':
                return self._extract_text_from_docx(file_path)
            elif file_extension == '.html' or file_extension == '.htm':
                return self._extract_text_from_html(file_path)
            elif file_extension == '.txt':
                return self._extract_text_from_txt(file_path)
            else:
                return self._extract_text_with_tika(file_path)
        except Exception as e:
            self.logger.error(f"Error extracting text from file {file_path}: {e}")
            raise

    def _extract_text_from_pdf(self, file_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            file_path: Local path to the PDF file
        
        Returns:
            Extracted text from the PDF file
        """
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.getNumPages()):
                text += reader.getPage(page_num).extractText()
        return text

    def _extract_text_from_docx(self, file_path: str) -> str:
        """
        Extract text from a Word document.
        
        Args:
            file_path: Local path to the Word document
        
        Returns:
            Extracted text from the Word document
        """
        return docx2txt.process(file_path)

    def _extract_text_from_html(self, file_path: str) -> str:
        """
        Extract text from an HTML file.
        
        Args:
            file_path: Local path to the HTML file
        
        Returns:
            Extracted text from the HTML file
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup.get_text()

    def _extract_text_from_txt(self, file_path: str) -> str:
        """
        Extract text from a plain text file.
        
        Args:
            file_path: Local path to the text file
        
        Returns:
            Extracted text from the text file
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def _extract_text_with_tika(self, file_path: str) -> str:
        """
        Extract text from a document using Apache Tika.
        
        Args:
            file_path: Local path to the document
        
        Returns:
            Extracted text from the document
        """
        raw = parser.from_file(file_path)
        return raw['content']
