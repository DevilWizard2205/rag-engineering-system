import re

from app.ingestion.chunking.chunk import Chunk
from app.ingestion.document import Document


class RecursiveChunker:

    def __init__(self, chunk_size: int = 500):
        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than 0"
            )

        self.chunk_size = chunk_size

    def _split_text(self, text: str) -> list[str]:

        if len(text) <= self.chunk_size:
            return [text.strip()]

        separators = [
            "\n\n",
            "\n",
            r"(?<=[.!?])\s+",
            " ",
        ]

        for separator in separators:

            if separator.startswith("(?<="):
                parts = re.split(separator, text)
            else:
                parts = text.split(separator)

            if len(parts) <= 1:
                continue

            chunks = []
            current = ""

            for part in parts:

                part = part.strip()

                if not part:
                    continue

                candidate = (
                    f"{current} {part}".strip()
                    if current
                    else part
                )

                if len(candidate) <= self.chunk_size:
                    current = candidate

                else:

                    if current:
                        chunks.append(current)

                    if len(part) <= self.chunk_size:
                        current = part

                    else:
                        chunks.extend(
                            self._split_text(part)
                        )
                        current = ""

            if current:
                chunks.append(current)

            return chunks

        # Final fallback: hard character split
        return [
            text[i:i + self.chunk_size].strip()
            for i in range(
                0,
                len(text),
                self.chunk_size
            )
            if text[i:i + self.chunk_size].strip()
        ]

    def chunk(self, document: Document) -> list[Chunk]:

        text = document.text.strip()

        if not text:
            return []

        text_chunks = self._split_text(text)

        chunks = []

        for index, chunk_text in enumerate(text_chunks):

            metadata = dict(document.metadata)

            metadata["chunk_index"] = index
            metadata["document_id"] = document.id
            metadata["content_hash"] = document.content_hash

            chunks.append(
                Chunk(
                    id=f"{document.id}_chunk_{index}",
                    text=chunk_text,
                    metadata=metadata,
                )
            )

        return chunks