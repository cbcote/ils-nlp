from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.text_normalizer import TextNormalizer

class TextPreprocessor:
    def __init__(self, config):
        self.cleaner = TextCleaner(config)
        self.normalizer = TextNormalizer(config)

    def preprocess(self, text):
        cleaned_text = self.cleaner.clean(text)
        normalized_text = self.normalizer.normalize(cleaned_text)
        return normalized_text
