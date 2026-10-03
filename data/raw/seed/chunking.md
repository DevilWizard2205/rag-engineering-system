# Chunking

Chunking is the process of dividing a document into smaller pieces before indexing it for retrieval. Retrieval systems generally operate on chunks rather than entire documents.

## Fixed-Size Chunking

Fixed-size chunking divides text into chunks based on a specified number of characters or tokens.

For example, a system can use a chunk size of 500 characters and an overlap of 50 characters. The overlap allows information near a chunk boundary to appear in adjacent chunks.

Fixed-size chunking is simple and predictable, but it can split related sentences or sections across chunk boundaries.

## Sentence Chunking

Sentence chunking groups complete sentences together until a configured maximum size is reached.

This approach attempts to preserve sentence boundaries and can produce chunks that are easier to interpret than arbitrary character slices.

## Recursive Chunking

Recursive chunking attempts to divide text using a hierarchy of separators.

A typical strategy can first attempt paragraph boundaries, then line boundaries, then sentence boundaries, and finally smaller separators if the resulting pieces are still too large.

Recursive chunking attempts to preserve larger semantic structures while still respecting a maximum chunk size.

## Chunk Size

Chunk size determines approximately how much text is placed into each chunk.

Very small chunks can lose surrounding context, while very large chunks can contain irrelevant information and increase the amount of context passed to later stages.

## Chunk Overlap

Chunk overlap is the amount of text shared between consecutive chunks.

Overlap can help preserve information that crosses chunk boundaries, but excessive overlap increases the number of chunks and therefore increases storage and retrieval costs.
