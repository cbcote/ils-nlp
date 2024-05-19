import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt') # Download Punkt tokenizer
nltk.download('stopwords') # Download stopwords
nltk.download('wordnet') # Download WordNet lemmatizer

class TextNormalizer:
    def __init__(self, config: dict):
        """Initialize text normalizer with configuration."""
        # Tokenization is enabled by default. If you want to disable it, set 'tokenization' to False in the config.
        self.tokenization = config['preprocessing'].get('tokenization', True)        
        # Lemmatization is enabled by default. If you want to disable it, set 'lemmatization' to False in the config.
        self.lemmatization = config['preprocessing'].get('lemmatization', False)
        # Stemming is enabled by default. If you want to disable it, set 'stemming' to False in the config.
        self.stemming = config['preprocessing'].get('stemming', True)
        # Set custom stopwords based on the configuration. Default is an empty list.
        self.custom_stopwords = config['preprocessing'].get('custom_stopwords', [])
        # Set stopwords based on the configuration. Default is English stopwords.
        self.stopwords = set(stopwords.words(config['preprocessing'].get('stopwords', 'english')))
        # Add custom stopwords to the set of stopwords.
        self.stopwords.update(self.custom_stopwords)
        # Initialize WordNet lemmatizer.
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def normalize(self, text: str) -> str:
        """
        Normalize text by tokenizing, lemmatizing, and removing stopwords.
        
        Args:
            text: Text to normalize
        
        Returns:
            Normalized text
        """
        # Tokenize text
        if self.tokenization:
            tokens = word_tokenize(text)
        else:
            tokens = text.split()

        # Lemmatize tokens and remove stopwords
        if self.lemmatization:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.lower() not in self.stopwords]
        elif self.stemming:
            # Stem tokens and remove stopwords
            tokens = [self.stemmer.stem(token) for token in tokens if token.lower() not in self.stopwords]
        else:
            tokens = [token for token in tokens if token.lower() not in self.stopwords]
        return ' '.join(tokens)
