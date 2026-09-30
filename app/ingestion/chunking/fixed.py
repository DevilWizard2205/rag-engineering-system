from app.ingestion.chunking.chunk import Chunk
from app.ingestion.document import Document


class FixedSizeChunker:

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        if overlap < 0:
            raise ValueError("overlap cannot be negative")

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document) -> list[Chunk]:

        text = document.text.strip()

        if not text:
            return []

        chunks = []

        start = 0
        chunk_index = 0

        step = self.chunk_size - self.overlap

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunk_id = (
                    f"{document.id}_chunk_{chunk_index}"
                )

                metadata = dict(document.metadata)

                metadata["chunk_index"] = chunk_index
                metadata["document_id"] = document.id
                metadata["content_hash"] = document.content_hash

                chunks.append(
                    Chunk(
                        id=chunk_id,
                        text=chunk_text,
                        metadata=metadata,
                    )
                )

            start += step
            chunk_index += 1

        return chunks