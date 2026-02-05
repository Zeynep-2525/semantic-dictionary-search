# Semantic Dictionary Search  
**Classical & Hybrid Information Retrieval–Based Dictionary System**

---

## 1. Problem Definition

Traditional dictionary systems rely on **exact word matching** or **prefix-based lookup**. These approaches fail when users do not know the exact lexical form of a word and instead describe its **meaning**.

This project aims to design and implement a **semantic dictionary search system** that retrieves words based on **meaning similarity**, starting from **classical Information Retrieval (IR) techniques** and evolving toward a **hybrid semantic architecture**.

---

## 2. Motivation

The project is intentionally built **from scratch**, without relying on high-level libraries for vectorization or similarity, in order to:

- Understand how semantic search systems work at a **fundamental level**
- Build an **explainable and mathematically grounded** search engine
- Connect core Computer Engineering topics:
  - Linear Algebra
  - Information Retrieval
  - Data Structures
  - Software Architecture

Rather than treating search as a black box, each component is implemented and tested explicitly.

---

## 3. Scope and Domain

### 3.1 Classical IR vs Modern Semantic Search

- **Classical Information Retrieval (IR):**  
  Uses statistical and algebraic models (TF–IDF, Vector Space Model, Cosine Similarity)

- **Neural / Embedding-Based Search:**  
  Uses dense vector representations learned from large corpora

This project **starts strictly in the classical IR domain**, then extends toward a **hybrid approach** combining both paradigms.

---

## 4. System Architecture

The system is composed of **two complementary layers**, implemented in different languages to reflect real-world modular systems.

---

### 4.1 Trie-Based Dictionary Layer (Java)

- Exact word lookup
- Prefix-based autocomplete
- Implemented using a **DLB Trie**
- Optimized for fast lookup and memory efficiency

📌 Implemented as a **separate Java project** and included via **Git submodule**.

---

### 4.2 Lexical Semantic Search Engine (Python – Implemented)

- Treats word definitions as documents
- Custom **text preprocessing pipeline**
- **TF–IDF vectorizer** implemented from scratch
- **Cosine similarity** for ranking
- Fully covered by **unit tests (pytest)**

This layer enables **meaning-based retrieval without neural models**.

---

### 4.3 Planned Semantic Extension (Hybrid Layer)

- Embedding-based semantic similarity
- Combination of TF–IDF scores and embedding similarity
- Modular design allows replacing or augmenting ranking strategies

---

## 5. High-Level Query Flow

User Query

├── Exact / Prefix Query ──▶ Trie Dictionary (Java)

└── Free-Text Query ───────▶ IR Search Engine (Python)

├── Preprocessing

├── TF–IDF Vectorization

└── Cosine Similarity Ranking


---

## 6. Mathematical Foundations

### 6.1 Vector Space Model

Each word definition is represented as a vector in a high-dimensional space where each dimension corresponds to a term in the vocabulary.

---

### 6.2 TF–IDF

- **Term Frequency (TF):** Importance of a term within a document  
- **Inverse Document Frequency (IDF):** Penalizes globally frequent terms  

Implemented explicitly to reinforce mathematical understanding.

---

### 6.3 Cosine Similarity

Similarity between vectors **A** and **B**:

cos(θ) = (A · B) / (||A|| ||B||)


Focuses on **direction**, not magnitude, making it suitable for textual similarity.

---

## 7. Implementation Overview

- Dictionary stored in JSON format
- Definitions treated as documents
- TF–IDF vectors computed programmatically
- Query processed through the same pipeline
- Results ranked by cosine similarity
- All core components tested with **pytest**

---

## 8. Testing Strategy

- Unit tests for:
  - Preprocessing
  - TF–IDF vectorization
  - Cosine similarity
  - Search engine behavior
- Tests executed via:
  ```bash
  pytest python/tests
Testing is used as a design tool, not just validation.

## 9. Current Limitations

Lexical gap between query and documents

No contextual or world knowledge

Static corpus (no learning)

These limitations are intentional and motivate the next development stage.

## 10. Roadmap / Future Work

Add embedding-based semantic search

Implement hybrid ranking (TF–IDF + embeddings)

Compare lexical vs semantic results

Optional lightweight API or CLI extensions

Scalability improvements (inverted index)

## 11. Learning Outcomes

This project demonstrates:

How semantic search works without neural networks

Practical application of linear algebra in IR systems

Modular, test-driven system design

Conscious engineering trade-offs

Evolution from classical IR to modern hybrid search

## 12. Dictionary Backbone

The trie-based dictionary engine is implemented in Java using a DLB Trie and included as a Git submodule under a separate organization repository.
