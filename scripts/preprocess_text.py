import argparse
from src.utils.config_loader import ConfigLoader
from src.utils.logger import Logger
from src.utils.helpers import clean_text, tokenize_text, remove_stopwords, lemmatize_tokens

def main():
    parser = argparse.ArgumentParser(description='Preprocess text.')
    parser.add_argument('--text', required=True, help='Text to preprocess')
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load_config('config/config.yaml')

    # Setup logging
    Logger.setup_logging(config_path='config/logging_config.yaml')
    logger = Logger.get_logger(__name__)

    # Preprocess the text
    text = args.text
    logger.info(f"Original text: {text}")

    cleaned_text = clean_text(text)
    logger.info(f"Cleaned text: {cleaned_text}")

    tokens = tokenize_text(cleaned_text)
    logger.info(f"Tokens: {tokens}")

    tokens = remove_stopwords(tokens, config['preprocessing']['stopwords'])
    logger.info(f"Tokens after stopword removal: {tokens}")

    if config['preprocessing']['lemmatization']:
        tokens = lemmatize_tokens(tokens)
        logger.info(f"Lemmatized tokens: {tokens}")

    preprocessed_text = ' '.join(tokens)
    logger.info(f"Preprocessed text: {preprocessed_text}")

if __name__ == '__main__':
    main()
