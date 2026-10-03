# RAG System Architecture

A Retrieval-Augmented Generation system can be organized as a pipeline containing ingestion, indexing, retrieval, reranking, generation, and evaluation components.

## Ingestion Layer

The ingestion layer loads source documents such as PDF, Markdown, TXT, and HTML files.

The documents are normalized into a common document representation containing text and metadata.

Content hashing can be used to identify duplicate documents and avoid unnecessary processing.

## Chunking Layer

Documents are divided into smaller chunks before indexing.

Different chunking strategies can be used, including fixed-size, sentence-based, and recursive chunking.

The selected chunking strategy can affect retrieval quality.

## Indexing Layer

The indexing layer prepares chunks for retrieval.

Dense embeddings are generated for vector search, while tokenized text can be indexed using a sparse retrieval algorithm such as BM25.

The resulting indexes allow the system to retrieve candidate chunks efficiently.

## Retrieval Layer

The retrieval layer receives a user query and searches the indexed chunks.

Dense retrieval identifies semantically similar chunks, while BM25 identifies chunks with relevant lexical terms.

A hybrid retriever can combine the rankings from both approaches using Reciprocal Rank Fusion.

## Reranking Layer

The initial candidate results can be passed to a cross-encoder reranker.

The reranker scores each query-chunk pair and reorders the candidates according to their estimated relevance.

The highest-ranked chunks are selected as the final context.

## Generation Layer

The final retrieved chunks are assembled into a context.

A language model receives the user question and the retrieved context and generates a grounded answer.

The generation prompt instructs the model to use the provided evidence and cite relevant context sources.

## Validation Layer

The generated answer can be checked for valid citations and citation coverage.

A confidence calculation can combine retrieval signals and citation signals.

If the available evidence is insufficient, the system can abstain instead of producing an unsupported answer.

## API Layer

A FastAPI service can expose the RAG system through HTTP endpoints.

Example endpoints include:

- `/health` for service health checks
- `/v1/ask` for answering questions
- `/v1/ingest` for adding documents
- `/v1/documents` for listing indexed documents

## Evaluation Layer

The evaluation layer runs a collection of golden questions through the RAG pipeline.

It records retrieval results, generated answers, citations, confidence values, and evaluation metrics.

This makes it possible to compare different chunking, retrieval, reranking, and generation configurations.

## Deployment

The complete system can be packaged using Docker and Docker Compose.

Containerization allows the API, supporting services, and configuration to be reproduced consistently across environments.
