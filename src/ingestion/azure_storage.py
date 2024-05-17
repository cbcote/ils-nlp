# src/ingestion/azure_storage.py
from azure.storage.blob import BlobServiceClient

class AzureStorage:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_name = container_name

    def upload_document(self, file_path: str) -> None:
        """
        Upload a document to Azure Blob Storage.
        
        Args:
            file_path: Local path to the document to upload
        
        Returns:
            None
        """
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_path)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"Uploaded {file_path} to {self.container_name}")
