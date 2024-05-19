import spacy

class NERModel:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text):
        doc = self.nlp(text)
        return [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
