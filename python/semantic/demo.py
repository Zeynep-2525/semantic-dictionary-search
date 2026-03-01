from python.semantic.embedding_model import EmbeddingModel
from python.semantic.embedding_index import EmbeddingIndex
from python.semantic.embedding_similarity import cosine_similarity
from python.semantic.data import DICTIONARY


def main():
    print("Semantic Dictionary Search (Embedding-based)")
    print("Type 'exit' to quit.\n")

    model = EmbeddingModel()
    index = EmbeddingIndex(model)

    index.build(DICTIONARY)

    while True:
        query = input("Query > ")
        if query.lower() == "exit":
            break

        query_vec = model.encode(query)

        scores = []
        for word, vec in index.embeddings.items():
            score = cosine_similarity(query_vec, vec)
            scores.append((word, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        print("\nTop results:")
        for word, score in scores[:5]:
            print(f"{word:<15}  {score:.4f}")
        print()


if __name__ == "__main__":
    main()
