from sklearn.metrics.pairwise import cosine_similarity
from semantic.embedding_model import EmbeddingModel
from semantic.embedding_index import build_index

def search(query, top_k=3):
    data, vectors = build_index()
    model = EmbeddingModel()

    query_vec = model.encode([query])
    similarities = cosine_similarity(query_vec, vectors)[0]

    results = sorted(
        zip(data, similarities),
        key=lambda x: x[1],
        reverse=True
    )

    return results[:top_k]


if __name__ == "__main__":
    results = search("yellow fruit")
    for text, score in results:
        print(f"{text} -> {score:.3f}")
