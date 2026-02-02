from preprocessing import preprocess_text
from tfidf import TfidfVectorizer
from cosine_similarity import cosine_similarity


class SearchEngine:
    def __init__(self, dictionary: dict[str, str]):
        self.raw_dictionary = dictionary
        self.processed_docs = {}
        self.document_vectors = {}

    def build_corpus(self):
        for word, definition in self.raw_dictionary.items():
            tokens = preprocess_text(definition)
            self.processed_docs[word] = tokens

    def build_index(self):
        self.build_corpus()
        self.vectorizer = TfidfVectorizer(self.processed_docs)
        self.vectorizer.build_vocabulary()
        self.vectorizer.compute_idf()

        for word, tokens in self.processed_docs.items():
            self.document_vectors[word] = self.vectorizer.vectorize(tokens)

    def search(self, query: str, top_k: int = 5):
        query_tokens = preprocess_text(query)
        query_vector = self.vectorizer.vectorize(query_tokens)

        scores = []

        for word, doc_vector in self.document_vectors.items():
            score = cosine_similarity(query_vector, doc_vector)
            if score > 0:
                scores.append((word, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
