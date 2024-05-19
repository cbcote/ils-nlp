import re
import nltk
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('stopwords')

class TextCleaner:
    def __init__(self, config):
        self.remove_digits = config['preprocessing'].get('remove_digits', True)
        self.remove_punctuation = config['preprocessing'].get('remove_punctuation', True)
        self.lowercase = config['preprocessing'].get('lowercase', True)
        self.remove_stopwords = config['preprocessing'].get('remove_stopwords', True)
        self.stop_words = set(stopwords.words('english'))

    def clean(self, text: str) -> str:
        """
        Clean text by removing digits and punctuation, and converting to lowercase.
        
        Args:
            text: Text to clean
        
        Returns:
            Cleaned text
        """
        if self.lowercase:
            text = text.lower()
        if self.remove_digits:
            text = re.sub(r'\d+', '', text)
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        if self.remove_stopwords:
            text = ' '.join([word for word in text.split() if word not in self.stop_words])
        return text
