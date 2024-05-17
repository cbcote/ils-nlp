import re

class TextCleaner:
    def __init__(self, config):
        self.remove_digits = config['preprocessing'].get('remove_digits', True)
        self.remove_punctuation = config['preprocessing'].get('remove_punctuation', True)

    def clean(self, text):
        if self.remove_digits:
            text = re.sub(r'\d+', '', text)
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text.lower()
