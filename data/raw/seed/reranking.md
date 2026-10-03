# Reranking

Reranking is a retrieval stage that reorders an initial set of candidate chunks according to their relevance to the user query.

## Candidate Retrieval

The first retrieval stages can retrieve a larger candidate set using dense retrieval, BM25, or a combination of both.

For example, a system may retrieve ten candidate chunks before applying a reranker.

## Cross-Encoder Reranking

A cross-encoder receives the query and a candidate chunk together and produces a relevance score for the pair.

Unlike a bi-encoder embedding model, the cross-encoder directly processes the query and document together when calculating relevance.

## Reranking Process

The reranker receives the query and the candidate chunks produced by the retrieval stage.

Each query-chunk pair is scored independently.

The candidates are then sorted by their relevance scores, and the highest-scoring chunks are selected for the final context.

## Retrieval Top-K vs Final Top-K

Retrieval top-k determines how many candidates are considered before reranking.

Final top-k determines how many chunks are passed to the generation stage after reranking.

Using a larger retrieval top-k followed by a smaller final top-k allows the reranker to select the strongest evidence from a broader candidate set.

## Benefits of Reranking

Reranking can improve the quality of the final context by moving highly relevant chunks above candidates that were initially ranked highly by lexical or embedding-based retrieval.

It can therefore reduce the amount of irrelevant information passed to the language model.

## Computational Cost

Cross-encoder reranking requires processing each query-chunk pair.

Increasing the number of candidates therefore increases reranking computation.

A practical system must balance retrieval recall against reranking latency and computational cost.
