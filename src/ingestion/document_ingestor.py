import os
from src.ingestion.text_extractor import TextExtractor
from src.ingestion.azure_storage import AzureStorage

class DocumentIngestor:
    def __init__(self, connection_string=None, container_name=None):
        self.text_extractor = TextExtractor()
        if connection_string and container_name:
            self.azure_storage = AzureStorage(connection_string, container_name)
        else:
            self.azure_storage = None

    def ingest_document(self, file_path):
        # Extract text from the document
        extracted_text = self.text_extractor.extract_text(file_path)
        
        # Upload the document to Azure Blob Storage if configured
        if self.azure_storage:
            self.azure_storage.upload_document(file_path)
        
        return extracted_text

    def ingest_from_directory(self, directory_path):
        texts = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                texts[filename] = self.ingest_document(file_path)
        return texts

    def list_files_in_directory(self, directory_path):
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
