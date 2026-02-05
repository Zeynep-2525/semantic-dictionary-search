import re
from typing import List


def preprocess_text(text: str) -> List[str]:
    """
    Basic preprocessing for IR pipeline:
    lowercase + remove non-alphanumeric + tokenize
    """
    text = text.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    tokens = text.split()

    # naive singularization
    tokens = [t[:-1] if t.endswith("s") else t for t in tokens]
    return tokens


class TextPreprocessor:
    def __init__(self, stopwords: List[str] | None = None):
        self.stopwords = set(stopwords) if stopwords else set()

    def normalize(self, text: str) -> str:
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
        text = self.normalize(text)
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return " ".join(tokens)
