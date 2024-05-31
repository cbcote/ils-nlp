import os
import sys
import nltk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the NLTK data path
nltk.data.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '/data/nltk_data')))

import json
import os
import argparse
from src.utils.logger import Logger
from src.utils.config_loader import ConfigLoader
from src.ingestion.text_extractor import TextExtractor
from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.text_normalizer import TextNormalizer
from src.annotation.annotator import Annotator

def save_to_file(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        if isinstance(data, str):
            f.write(data)
        else:
            json.dump(data, f, ensure_ascii=False, indent=4)

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
        text_extractor = TextExtractor(config)
        text_cleaner = TextCleaner(config)
        text_normalizer = TextNormalizer(config)
        annotator = Annotator()

        # Extract text
        logger.info("Extracting text from the document")
        raw_text = text_extractor.extract_text(args.file)
        extracted_path = os.path.join('data', 'extracted', f"{os.path.basename(args.file)}.txt")
        save_to_file(raw_text, extracted_path)
        logger.info(f"Extracted text saved to {extracted_path}")

        # Clean text
        logger.info("Cleaning the extracted text")
        cleaned_text = text_cleaner.clean(raw_text)
        cleaned_path = os.path.join('data', 'cleaned', f"{os.path.basename(args.file)}.txt")
        save_to_file(cleaned_text, cleaned_path)
        logger.info(f"Cleaned text saved to {cleaned_path}")

        # Normalize text
        logger.info("Normalizing the cleaned text")
        normalized_text = text_normalizer.normalize(cleaned_text)
        interim_path = os.path.join('data', 'interim', f"{os.path.basename(args.file)}.txt")
        save_to_file(normalized_text, interim_path)
        logger.info(f"Normalized text saved to {interim_path}")

        # Generate annotations
        logger.info("Generating annotations")
        annotations = annotator.generate_annotations(normalized_text)

        # Save annotations to JSON
        document_id = os.path.basename(args.file).split('.')[0]
        annotation_data = {
            "document_id": document_id,
            "text": normalized_text,
            "annotations": [{"start": start, "end": end, "label": label} for start, end, label in annotations]
        }
        output_path = os.path.join('data', 'annotated', f"{document_id}_annotations.json")
        save_to_file(annotation_data, output_path)

        logger.info(f"Annotations saved to {output_path}")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        raise

if __name__ == '__main__':
    main()
