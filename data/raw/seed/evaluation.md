# Evaluation

Evaluation measures how well a Retrieval-Augmented Generation system retrieves evidence and produces answers supported by that evidence.

## Golden Questions

A golden evaluation dataset contains questions with expected answers or expected supporting information.

A useful evaluation set should contain different types of questions rather than only straightforward questions.

## Straightforward Questions

Straightforward questions can usually be answered directly from a single relevant chunk.

These questions test whether the retrieval system can find obvious supporting evidence.

## Multi-Hop Questions

Multi-hop questions require information from multiple pieces of evidence.

A system must retrieve the relevant chunks and combine their information to answer these questions correctly.

## Unanswerable Questions

Unanswerable questions ask for information that is not present in the knowledge base.

A grounded RAG system should recognize that the available documents do not contain enough information instead of inventing an answer.

## Ambiguous Questions

Ambiguous questions can have multiple interpretations or may not provide enough detail to identify the intended information.

These questions test whether the system handles uncertainty appropriately.

## Retrieval Metrics

Retrieval metrics measure whether relevant evidence appears in the retrieved results.

Hit@K measures whether the expected relevant chunk appears within the top K retrieved results.

## Answer Correctness

Answer correctness measures whether the generated answer correctly addresses the question according to the expected answer or reference information.

## Faithfulness

Faithfulness measures whether the generated answer is supported by the retrieved context.

An answer can be relevant to the question while still containing claims that are not supported by the retrieved evidence.

## Citation Accuracy

Citation accuracy measures whether the citations in the generated answer correctly refer to the evidence supporting the associated claims.

## Evaluation Pipeline

An evaluation pipeline can run a collection of golden questions through the complete RAG system.

The pipeline can record retrieval results, generated answers, citations, confidence scores, and evaluation metrics.

Comparing these results across different chunking and retrieval configurations can help identify which system components affect performance.
