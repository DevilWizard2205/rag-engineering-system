# Retrieval

Retrieval is the stage of a Retrieval-Augmented Generation system that searches a knowledge base for information relevant to a user query.

## Dense Retrieval

Dense retrieval represents documents and queries as numerical embedding vectors. A query is embedded into the same vector space as the stored document chunks. Similarity between the query vector and document vectors is then used to identify relevant chunks.

Dense retrieval is useful when the wording of a query differs from the wording used in the source documents because embeddings can capture semantic similarity.

## Sparse Retrieval

Sparse retrieval uses lexical information from the text. BM25 is a common sparse retrieval algorithm. It scores documents based on the occurrence and importance of query terms.

BM25 can be particularly useful when exact terms, names, identifiers, or technical keywords appear in both the query and the document.

## Hybrid Retrieval

Hybrid retrieval combines multiple retrieval methods. A system can combine dense retrieval with BM25 so that semantic similarity and lexical matching both contribute to candidate selection.

Combining retrieval methods can improve robustness because the methods capture different types of relevance.

## Retrieval Top-K

The retrieval top-k parameter controls how many candidates are retrieved before later processing stages. A larger candidate set can increase the chance of retrieving relevant evidence, but it also increases the amount of data that later stages must process.
