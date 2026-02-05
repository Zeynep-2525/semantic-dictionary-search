from ir.search_engine import SearchEngine

def test_semantic_search_basic():
    dictionary = {
        "malaria": "A disease caused by mosquitoes",
        "table": "A piece of furniture"
    }

    engine = SearchEngine(dictionary)
    engine.build_index()

    results = engine.search("mosquito disease", top_k=1)

    assert results[0][0] == "malaria"
