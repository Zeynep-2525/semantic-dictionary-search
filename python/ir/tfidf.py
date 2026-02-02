import math
from collections import Counter
class TfidfVectorizer:
    def __init__(self, documents: dict[str, list[str]]):
        """
        documents:
        {
            "word1": ["token1", "token2", ...],
            "word2": [...]
        }
        """
        self.documents = documents
        self.vocabulary = set()
        self.idf = {}
    def build_vocabulary(self):
        for tokens in self.documents.values():
            for token in tokens:
                self.vocabulary.add(token)
    def compute_idf(self):
        total_docs = len(self.documents)

        for term in self.vocabulary:
            doc_count = 0
            for tokens in self.documents.values():
                if term in tokens:
                    doc_count += 1

            self.idf[term] = math.log(total_docs / (1 + doc_count))
    def compute_tf(self, tokens: list[str]) -> dict[str, float]:
        tf = {}
        counts = Counter(tokens)
        total = len(tokens)

        for term, count in counts.items():
            tf[term] = count / total

        return tf
    def vectorize(self, tokens: list[str]) -> dict[str, float]:
        tf = self.compute_tf(tokens)
        vector = {}

        for term in tf:
            if term in self.idf:
                vector[term] = tf[term] * self.idf[term]

        return vector
