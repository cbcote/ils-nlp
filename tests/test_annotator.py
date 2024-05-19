import unittest
from src.annotation.annotator import Annotator

class TestAnnotator(unittest.TestCase):
    def setUp(self):
        self.annotator = Annotator()

    def test_generate_annotations(self):
        text = "Vista Re Ltd. is offering Series 2021-1 Class A Principal At-Risk Variable Rate Notes."
        annotations = self.annotator.generate_annotations(text)
        self.assertTrue(len(annotations) > 0)

if __name__ == '__main__':
    unittest.main()
