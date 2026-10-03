# Embeddings

Embeddings are numerical representations of text that place semantically related pieces of text closer together in a vector space.

## Document Embeddings

During indexing, each document chunk can be converted into an embedding vector. The vector is stored alongside the chunk so that it can later be searched using vector similarity.

## Query Embeddings

When a user submits a query, the query is converted into an embedding using the same embedding model used for the document chunks.

The query vector can then be compared with stored document vectors to identify semantically similar chunks.

## Vector Similarity

A vector database can compare a query embedding with stored embeddings and return the chunks that are most similar to the query.

Cosine similarity is one common measure used for comparing embedding vectors.

## Embedding Model

The quality of dense retrieval depends partly on the embedding model. An embedding model should produce representations that capture useful semantic relationships between queries and documents.

Changing the embedding model can therefore change retrieval results even when the underlying documents remain unchanged.

## Embedding Dimensions

An embedding vector has a fixed number of numerical dimensions determined by the embedding model.

Different embedding models can produce vectors with different dimensions. Vectors stored in the same vector collection must use a compatible dimensionality.

## Indexing and Retrieval

Embeddings are normally generated during document indexing and stored in a vector database. During retrieval, only the query needs to be embedded again before performing the vector search.

This avoids recomputing document embeddings for every user query.
