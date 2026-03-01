from semantic.embedding_model import EmbeddingModel
from semantic.data import load_data

def build_index():
    data = load_data()
    model = EmbeddingModel()
    vectors = model.encode(data)
    return data, vectors
