from ir.preprocessing import preprocess_text

def test_preprocess_basic():
    text = "Malaria, Disease!"
    tokens = preprocess_text(text)
    assert tokens == ["malaria", "disease"]
