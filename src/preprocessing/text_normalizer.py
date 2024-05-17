import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TextNormalizer:
    def __init__(self, config):
        self.lemmatization = config['preprocessing'].get('lemmatization', True)
        self.stopwords = set(stopwords.words(config['preprocessing'].get('stopwords', 'english')))
        self.lemmatizer = WordNetLemmatizer()

    def normalize(self, text):
        tokens = word_tokenize(text)
        if self.lemmatization:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stopwords]
        return ' '.join(tokens)
