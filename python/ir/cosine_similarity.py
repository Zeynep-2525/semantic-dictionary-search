import math

def cosine_similarity(vec1: dict[str, float], vec2: dict[str, float]) -> float:
    dot_product = 0.0

    for term in vec1:
        if term in vec2:
            dot_product += vec1[term] * vec2[term]

    norm1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
    norm2 = math.sqrt(sum(value ** 2 for value in vec2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)
