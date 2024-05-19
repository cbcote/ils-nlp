import unittest
from src.annotation.rule_based_annotator import RuleBasedAnnotator

class TestRuleBasedAnnotator(unittest.TestCase):
    def setUp(self):
        self.annotator = RuleBasedAnnotator()

    def test_find_issuer(self):
        text = "Vista Re Ltd. is offering Series 2021-1 Class A Principal At-Risk Variable Rate Notes."
        annotations = self.annotator.find_issuer(text)
        self.assertTrue(len(annotations) > 0)

if __name__ == '__main__':
    unittest.main()
