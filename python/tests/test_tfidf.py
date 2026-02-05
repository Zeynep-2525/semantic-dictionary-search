from ir.tfidf import TfidfVectorizer

def test_tfidf_vector_non_empty():
    docs = {
        "a": ["cat", "animal"],
        "b": ["dog", "animal"]
    }

    tfidf = TfidfVectorizer(docs)
    tfidf.build_vocabulary()
    tfidf.compute_idf()

    vector = tfidf.vectorize(["cat", "animal"])
    assert len(vector) > 0
