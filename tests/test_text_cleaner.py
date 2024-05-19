# tests/test_text_cleaner.py
import unittest
from src.preprocessing.text_cleaner import TextCleaner

class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        config = {
            'preprocessing': {
                'remove_digits': True,
                'remove_punctuation': True
            }
        }
        self.cleaner = TextCleaner(config)

    def test_clean_text(self):
        text = "This is a test text with numbers 123 and punctuation!."
        cleaned_text = self.cleaner.clean(text)
        expected_text = "this is a test text with numbers and punctuation"
        self.assertEqual(cleaned_text, expected_text)

if __name__ == '__main__':
    unittest.main()
