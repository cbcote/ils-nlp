from src.annotation.ner import NERModel
from src.annotation.rule_based_annotator import RuleBasedAnnotator

class Annotator:
    def __init__(self):
        self.ner_model = NERModel()
        self.rule_based_annotator = RuleBasedAnnotator()

    def generate_annotations(self, text):
        annotations = self.ner_model.extract_entities(text)
        annotations.extend(self.rule_based_annotator.find_issuer(text))
        return annotations
