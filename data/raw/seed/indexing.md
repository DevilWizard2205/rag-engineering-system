# Indexing

Indexing is the process of preparing document chunks so that they can be searched efficiently during retrieval.

## Chunk Preparation

Before indexing, documents are divided into chunks and each chunk receives an identifier and metadata.

The metadata can include the original document identifier, chunk position, source, file type, and content hash.

## Dense Index

A dense index stores embedding vectors representing document chunks.

During indexing, an embedding model converts each chunk into a numerical vector.

The vectors are stored in a vector database such as ChromaDB.

## Sparse Index

A sparse index stores lexical information that can be used by algorithms such as BM25.

The text of each chunk is tokenized and added to the sparse retrieval index.

## Vector Database

A vector database stores embeddings together with the corresponding chunk text and metadata.

When a query embedding is provided, the vector database can return the chunks whose vectors are most similar to the query vector.

## Persistent Storage

Persistent vector storage allows indexed data to survive after the application process stops.

The storage location should normally be treated as application data rather than source code.

## Idempotent Indexing

An indexing operation should avoid creating duplicate entries when the same document is processed repeatedly.

Stable document and chunk identifiers can be used to detect existing entries.

Content hashes can also help determine whether a document has changed since its previous indexing operation.

## Re-indexing

When a document changes, the system should be able to update its indexed chunks.

A re-indexing process can remove or replace the old chunks and then index the new chunks.

This keeps the retrieval index synchronized with the source documents.

## Indexing Pipeline

A typical indexing pipeline is:

1. Load documents.
2. Normalize metadata.
3. Detect duplicates.
4. Split documents into chunks.
5. Generate embeddings.
6. Update the dense index.
7. Update the sparse index.
8. Store metadata required for retrieval and debugging.

## Indexing and Retrieval Consistency

The dense and sparse indexes should represent the same version of the underlying chunks.

If one index contains outdated chunks while another contains newer chunks, hybrid retrieval can produce inconsistent results.
