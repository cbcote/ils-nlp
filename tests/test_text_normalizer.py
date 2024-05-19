import unittest
from src.preprocessing.text_normalizer import TextNormalizer

class TestTextNormalizer(unittest.TestCase):
    def setUp(self):
        config = {
            'preprocessing': {
                'tokenization': True,
                'lemmatization': True,
                'stemming': True,
                'stopwords': 'english',
                'custom_stopwords': ['common', 'stopword']
            }
        }
        self.normalizer = TextNormalizer(config)

    def test_normalize_text_with_lemmatization(self):
        text = "This is a test text with some common stopwords and lemmatization."
        normalized_text = self.normalizer.normalize(text)
        expected_text = "test text stopword lemmatization"  # Assuming lemmatization takes precedence
        self.assertEqual(normalized_text, expected_text)

    def test_normalize_text_with_stemming(self):
        # Test with stemming enabled and lemmatization disabled
        config = {
            'preprocessing': {
                'tokenization': True,
                'lemmatization': False,
                'stemming': True,
                'stopwords': 'english',
                'custom_stopwords': ['common', 'stopword']
            }
        }
        normalizer = TextNormalizer(config)
        text = "This is a test text with some common stopwords and lemmatization."
        normalized_text = normalizer.normalize(text)
        expected_text = "test text stopword lemmat"  # Expected result with stemming
        self.assertEqual(normalized_text, expected_text)

if __name__ == '__main__':
    unittest.main()
