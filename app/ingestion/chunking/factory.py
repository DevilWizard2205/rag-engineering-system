from app.ingestion.chunking.fixed import FixedSizeChunker
from app.ingestion.chunking.sentence import SentenceChunker
from app.ingestion.chunking.recursive import RecursiveChunker


def get_chunker(
    strategy: str,
    **kwargs
):
    if strategy == "fixed":
        return FixedSizeChunker(**kwargs)

    if strategy == "sentence":
        return SentenceChunker(**kwargs)

    if strategy == "recursive":
        return RecursiveChunker(**kwargs)

    raise ValueError(
        f"Unknown chunking strategy: {strategy}"
    )