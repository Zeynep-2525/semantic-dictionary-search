from ir.search_engine import SearchEngine


def main():
    dictionary = {
        "malaria": "A disease caused by mosquitoes",
        "table": "A piece of furniture with flat top",
        "python": "A programming language used for data science",
        "virus": "A microscopic infectious agent"
    }

    engine = SearchEngine(dictionary)
    engine.build_index()

    print("Semantic Dictionary Search (TF-IDF based)")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Query> ")
        if query.lower() == "exit":
            break

        results = engine.search(query, top_k=3)

        if not results:
            print("No results found.\n")
            continue

        for word, score in results:
            print(f"{word:<10} score={score:.4f}")
        print()


if __name__ == "__main__":
    main()
