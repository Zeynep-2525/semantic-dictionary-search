import re
from typing import List

class TextPreprocessor:
    def __init__(self, stopwords: List[str] | None = None):
        self.stopwords = set(stopwords) if stopwords else set()

    def normalize(self, text: str) -> str:
        """
        Lowercase + remove non-alphabetic characters
        """
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text

    def tokenize(self, text: str) -> List[str]:
        return text.split()

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        if not self.stopwords:
            return tokens
        return [t for t in tokens if t not in self.stopwords]

    def preprocess(self, text: str) -> str:
        """
        Full preprocessing pipeline:
        raw text -> cleaned string
        """
        text = self.normalize(text)
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return " ".join(tokens)
