# scripts/annotate_document.py
import json
import argparse
from src.utils.config_loader import ConfigLoader
from src.ingestion.text_extractor import TextExtractor
from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.text_normalizer import TextNormalizer
from src.annotation.annotator import Annotator

def main():
    parser = argparse.ArgumentParser(description='Annotate offering circular document.')
    parser.add_argument('--file', required=True, help='Path to the document file')
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load_config('config/config.yaml')

    # Initialize components
    text_extractor = TextExtractor()
    text_cleaner = TextCleaner()
    text_normalizer = TextNormalizer()
    annotator = Annotator()

    # Extract, clean, and normalize text
    raw_text = text_extractor.extract_text(args.file)
    cleaned_text = text_cleaner.clean_text(raw_text)
    normalized_text = text_normalizer.normalize_text(cleaned_text)

    # Generate annotations
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
    print(f"Annotations saved to {output_path}")

if __name__ == '__main__':
    main()
