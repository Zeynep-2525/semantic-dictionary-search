from ir.cosine_similarity import cosine_similarity

def test_cosine_identical_vectors():
    v = {"a": 1.0, "b": 2.0}
    score = cosine_similarity(v, v)
    assert score == 1.0
