# Generation

Generation is the stage of a Retrieval-Augmented Generation system that produces an answer using information retrieved from the knowledge base.

## Context

The retrieved chunks are assembled into a context that is provided to the language model.

The context should contain the most relevant evidence for answering the user's question.

## Grounded Generation

A grounded generation system instructs the language model to answer using the retrieved context rather than relying on unsupported outside information.

Grounding reduces the risk of generating information that is not supported by the indexed documents.

## Prompt Construction

The prompt contains the user's question together with the retrieved context.

A clear prompt can instruct the language model to use only the provided context and to indicate when the available information is insufficient.

## Citations

Retrieved context can be assigned source numbers such as `[1]`, `[2]`, and `[3]`.

The generated answer can reference these source numbers to show which retrieved pieces of evidence support each statement.

## Citation Validation

Citation validation checks whether citations produced by the language model refer to valid context sources.

For example, if only five context sources were provided, a citation such as `[7]` is invalid.

## Citation Coverage

Citation coverage measures how much of the available context is referenced by the generated answer.

Coverage can help identify answers that provide citations but do not reference enough of the retrieved evidence.

## Abstention

A RAG system can abstain when the available evidence is insufficient to answer a question reliably.

Instead of generating an unsupported answer, the system can return a message explaining that the provided documents do not contain enough information.
