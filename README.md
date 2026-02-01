# Semantic Dictionary Search  
**Classical Information Retrieval–Based Dictionary System**

---

## 1. Problem Definition

Traditional dictionary search systems rely primarily on **exact word matching** or **prefix-based lookup**. These approaches are insufficient when users do not know the exact lexical form of a word but can instead describe its **meaning**.

This project aims to design and implement a **semantic dictionary search system** that retrieves words based on **meaning similarity rather than string equality**, using **classical Information Retrieval (IR) techniques**.

---

## 2. Motivation

This project is intentionally built **without deep learning or neural embeddings** in order to:

- Understand how semantic search systems were designed **before modern AI models**
- Build an **explainable, mathematically grounded** search engine
- Strengthen the connection between core Computer Engineering courses:
  - Linear Algebra
  - Probability & Statistics
  - Data Structures and Algorithms

Instead of black-box neural representations, the system relies on **TF–IDF**, the **Vector Space Model**, and **Cosine Similarity** to achieve semantic relevance.

---

## 3. Scope and Domain

### 3.1 Information Retrieval vs Machine Learning

- **Information Retrieval (IR):**  
  Ranks documents using statistical and algebraic models

- **Machine Learning–based Search:**  
  Learns representations via optimization and training data

This project belongs **strictly to the classical IR domain** and does not involve model training or learned embeddings.

---

## 4. System Architecture

The system consists of **two complementary layers**:

### 4.1 Trie-Based Dictionary Layer (Java)

- Exact word lookup
- Prefix-based autocomplete
- High-performance retrieval using a **DLB Trie**
- Optimized for memory efficiency and fast lookup

*(Implemented as a separate Java-based project and included as a Git submodule.)*

---

### 4.2 Semantic Search Engine (IR Layer – Python)

- Processes word definitions as documents
- Applies TF–IDF vectorization
- Ranks candidate words using cosine similarity

---

### 4.3 High-Level Flow

User Query

├── Exact / Prefix Query ──▶ Trie Dictionary

└── Free-Text Query ───────▶ Semantic Search Engine

├── Preprocessing

├── TF–IDF Vectorization

└── Similarity Ranking


---

## 5. Mathematical Foundations

### 5.1 Vector Space Model

Each word definition is represented as a vector in a high-dimensional space, where each dimension corresponds to a term in the vocabulary.

---

### 5.2 TF–IDF

- **Term Frequency (TF):** Measures the importance of a term within a document  
- **Inverse Document Frequency (IDF):** Reduces the weight of terms that appear frequently across documents

---

### 5.3 Cosine Similarity

Similarity between a query vector **A** and a document vector **B** is computed as:

cos(θ) = (A · B) / (||A|| ||B||)


This metric focuses on **vector orientation**, not magnitude, making it suitable for textual similarity.

---

## 6. Implementation Overview

- Dictionary data stored in JSON format
- Word definitions treated as documents
- TF–IDF vectors computed offline
- Query processed using the same preprocessing pipeline
- Results ranked by cosine similarity score

---

## 7. Evaluation Strategy

- Manually selected test queries
- Expected relevant words defined by the developer
- Ranking behavior analyzed qualitatively

This evaluation prioritizes **interpretability and reasoning clarity**, not benchmark-based accuracy.

---

## 8. Limitations

- Cannot capture deep contextual or world knowledge
- Sensitive to vocabulary mismatch
- No learning or adaptation over time

These limitations are **intentional** and aligned with the project’s educational goals.

---

## 9. Future Work

- Replace TF–IDF with word embeddings
- Compare classical IR and neural semantic search approaches
- Introduce an inverted index for scalability
- Explore hybrid ranking strategies (Trie + IR + ML)

---

## 10. Learning Outcomes

This project demonstrates:

- Practical application of **Linear Algebra** in software systems
- Core **Information Retrieval** concepts and architecture
- Design of an **explainable semantic search system**
- Engineering trade-offs and system-level decision making

---

## 11. Dictionary Backbone

The trie-based dictionary component is implemented in Java using a **DLB Trie** and is included in this repository as a **Git submodule**.
