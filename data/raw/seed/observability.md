# Observability

Observability helps developers understand what a RAG system is doing internally and diagnose problems when retrieval or generation produces unexpected results.

## Retrieval Debugging

A retrieval system should expose enough information to understand why particular chunks were selected.

Useful debugging information includes the query, retrieved chunk identifiers, retrieval scores, and ranking positions.

## Dense Retrieval Results

Dense retrieval debugging can record the query embedding search results and the similarity scores returned by the vector database.

This helps determine whether relevant chunks are being retrieved through semantic similarity.

## BM25 Results

BM25 debugging can record the lexical ranking and BM25 scores for retrieved chunks.

This makes it possible to determine whether exact terms in the query are contributing to retrieval.

## Hybrid Retrieval Results

A hybrid retriever can record the rankings produced by each retrieval method before fusion.

The system can also record the Reciprocal Rank Fusion scores and the final candidate ordering.

This allows developers to determine which retrieval method contributed a particular candidate.

## Reranking Results

Reranking diagnostics can record the candidates passed to the cross-encoder and the relevance score assigned to each candidate.

Comparing the ranking before and after reranking can reveal whether the reranker is changing the candidate order.

## Generation Diagnostics

Generation diagnostics can record the retrieved context, generated answer, extracted citations, citation validation results, and confidence values.

This information helps identify whether an incorrect answer originated from retrieval, generation, or citation handling.

## Latency

The system can measure the time spent in different pipeline stages.

Useful measurements include ingestion time, embedding time, dense retrieval latency, BM25 latency, reranking latency, and generation latency.

Breaking total latency into individual stages makes performance bottlenecks easier to identify.

## Error Logging

Errors should be logged with enough context to diagnose failures while avoiding sensitive information.

Examples include document loading failures, embedding errors, vector database errors, model errors, and API request failures.

## Request Tracing

A request identifier can be associated with each API request.

The identifier can then be included in logs produced by different pipeline components, making it easier to trace a request from the API through retrieval and generation.

## Evaluation Observability

Evaluation runs should record configuration information such as the chunking strategy, retrieval top-k, reranking configuration, and generation model.

Recording these settings makes it possible to compare evaluation results across different system configurations.
