# scripts/preprocess_text.py
import argparse
import yaml
from src.preprocessing.text_preprocessor import TextPreprocessor

def main():
    parser = argparse.ArgumentParser(description='Preprocess text.')
    parser.add_argument('--text', required=True, help='Text to preprocess')
    args = parser.parse_args()

    # Load configuration
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Initialize the TextPreprocessor
    preprocessor = TextPreprocessor(config)
    
    # Preprocess the text
    preprocessed_text = preprocessor.preprocess(args.text)
    print(preprocessed_text)

if __name__ == '__main__':
    main()
