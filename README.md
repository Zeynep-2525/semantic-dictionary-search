# Semantic Dictionary Search (Classical IR Approach)

## 1. Problem Definition

Traditional dictionary search relies on **exact word matching** or simple prefix-based lookup. This approach fails when users do not know the exact word they are looking for but can describe its **meaning**.

This project aims to design and implement a **semantic dictionary search system** that retrieves words based on **meaning similarity**, not exact string matching, using **classical Information Retrieval (IR)** techniques.

---

## 2. Motivation

This project is intentionally designed using **pre–deep learning IR techniques** to:

* Understand how semantic search worked *before modern AI models*
* Build an explainable and mathematically grounded system
* Connect core Computer Engineering courses (Linear Algebra, Probability, Data Structures)

Rather than using black-box neural embeddings, the system uses **TF–IDF**, **Vector Space Model**, and **Cosine Similarity** to achieve semantic relevance.

---

## 3. Background

### 3.1 Information Retrieval vs Machine Learning

* **Information Retrieval (IR):** Uses statistical and algebraic models to rank documents
* **Machine Learning-based Search:** Learns embeddings from data using optimization

This project belongs strictly to the **classical IR** domain.

---

## 4. System Architecture

The system combines two complementary components:

1. **Trie Data Structure**

   * Used for exact match and prefix-based search
   * Enables fast lookup and autocomplete functionality

2. **Semantic Search Engine (IR Layer)**

   * Uses TF–IDF vectorization on word definitions
   * Computes similarity between query and definitions

High-level flow:

```
User Query
   ├── Prefix / Exact Match → Trie
   └── Free Text Query → Semantic Search Engine
                           ├── Preprocessing
                           ├── Vectorization (TF–IDF)
                           └── Similarity Ranking
```

---

## 5. Mathematical Foundation

### 5.1 Vector Space Model

Each word definition is represented as a vector in a high-dimensional space.

### 5.2 TF–IDF

* **Term Frequency (TF):** Measures importance of a term within a document
* **Inverse Document Frequency (IDF):** Reduces weight of common terms

### 5.3 Cosine Similarity

Used to measure similarity between query and definition vectors:

cos(θ) = (A · B) / (||A|| ||B||)

---

## 6. Implementation Overview

* Input data stored in **JSON format**
* Trie nodes store references to dictionary entries
* TF–IDF vectors are computed from definitions
* Query is processed through the same pipeline
* Results ranked by cosine similarity score

---

## 7. Evaluation Strategy

* Manually selected test queries
* Expected relevant words defined by the developer
* Ranking quality observed and analyzed

This evaluation focuses on **interpretability**, not benchmark accuracy.

---

## 8. Limitations

* Cannot capture deep contextual meaning
* Sensitive to vocabulary mismatch
* No learning or adaptation over time

These limitations are intentional and documented.

---

## 9. Future Work

* Replace TF–IDF with word embeddings
* Compare classical IR vs neural semantic search
* Add inverted index for scalability
* Hybrid ranking (Trie + IR + ML)

---

## 10. Learning Outcomes

This project demonstrates:

* Practical use of Linear Algebra in software systems
* Core IR concepts and system design
* Explainable semantic search architecture
* Engineering decision-making and trade-offs
