import re
from typing import List


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isalnum() or ch.isspace())
    tokens = text.split()

    normalized = []
    for t in tokens:
        if t.endswith("es"):
            normalized.append(t[:-2])
        elif t.endswith("s"):
            normalized.append(t[:-1])
        else:
            normalized.append(t)

    return normalized



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
