# scripts/annotate_document.py
import json
import argparse
from src.utils.logger import Logger
from src.utils.config_loader import ConfigLoader
from src.ingestion.text_extractor import TextExtractor
from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.text_normalizer import TextNormalizer
from src.annotation.annotator import Annotator

def main():
    Logger.setup_logging()
    logger = Logger.get_logger(__name__)
    
    parser = argparse.ArgumentParser(description='Annotate offering circular document.')
    parser.add_argument('--file', required=True, help='Path to the document file')
    args = parser.parse_args()

    logger.info(f"Started annotation for file: {args.file}")

    try:
        # Load configuration
        config = ConfigLoader.load_config('config/config.yaml')
        logger.info("Configuration loaded successfully")

        # Initialize components
        text_extractor = TextExtractor()
        text_cleaner = TextCleaner(config)
        text_normalizer = TextNormalizer(config)
        annotator = Annotator()

        # Extract, clean, and normalize text
        logger.info("Extracting text from the document")
        raw_text = text_extractor.extract_text(args.file)

        logger.info("Cleaning the extracted text")
        cleaned_text = text_cleaner.clean(raw_text)

        logger.info("Normalizing the cleaned text")
        normalized_text = text_normalizer.normalize(cleaned_text)

        # Generate annotations
        logger.info("Generating annotations")
        annotations = annotator.generate_annotations(normalized_text)

        # Save annotations to JSON
        document_id = args.file.split('/')[-1].split('.')[0]
        annotation_data = {
            "document_id": document_id,
            "text": normalized_text,
            "annotations": [{"start": start, "end": end, "label": label} for start, end, label in annotations]
        }
        output_path = f"data/annotated/{document_id}_annotations.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(annotation_data, f, ensure_ascii=False, indent=4)

        logger.info(f"Annotations saved to {output_path}")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        raise

if __name__ == '__main__':
    main()
