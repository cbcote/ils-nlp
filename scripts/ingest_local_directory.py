import argparse
from src.utils.config_loader import ConfigLoader
from src.ingestion.document_ingestor import DocumentIngestor

def main():
    parser = argparse.ArgumentParser(description='Ingest documents from a local directory.')
    parser.add_argument('--directory', required=True, help='Path to the directory containing documents')
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load_config('config/config.yaml')

    # Initialize the DocumentIngestor
    ingestor = DocumentIngestor()

    # Ingest documents from the local directory
    texts = ingestor.ingest_from_directory(args.directory)
    for filename, text in texts.items():
        print(f"{filename}: {text[:100]}...")  # Print the first 100 characters of each extracted text

if __name__ == '__main__':
    main()
