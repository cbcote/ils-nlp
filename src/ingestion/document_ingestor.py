from src.ingestion.text_extractor import TextExtractor
from src.ingestion.azure_storage import AzureStorage

class DocumentIngestor:
    def __init__(self, connection_string, container_name):
        self.text_extractor = TextExtractor()
        self.azure_storage = AzureStorage(connection_string, container_name)

    def ingest_document(self, file_path):
        # Extract text from the document
        extracted_text = self.text_extractor.extract_text(file_path)
        
        # Upload the document to Azure Blob Storage
        self.azure_storage.upload_document(file_path)
        
        return extracted_text
