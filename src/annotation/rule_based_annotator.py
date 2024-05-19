import re

class RuleBasedAnnotator:
    def find_issuer(self, text):
        issuer_pattern = re.compile(r'Vista Re Ltd\.', re.IGNORECASE)
        matches = issuer_pattern.finditer(text)
        return [(match.start(), match.end(), "Issuer") for match in matches]
