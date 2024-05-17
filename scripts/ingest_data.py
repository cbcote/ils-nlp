import argparse
import yaml
from src.ingestion.document_ingestor import DocumentIngestor

def main():
    parser = argparse.ArgumentParser(description='Ingest documents into the system.')
    parser.add_argument('--file', required=True, help='Path to the file to ingest')
    args = parser.parse_args()

    # Load configuration
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Initialize the DocumentIngestor
    ingestor = DocumentIngestor(config['azure']['connection_string'], config['azure']['container_name'])
    
    # Ingest the document
    extracted_text = ingestor.ingest_document(args.file)
    print(extracted_text)

if __name__ == '__main__':
    main()
