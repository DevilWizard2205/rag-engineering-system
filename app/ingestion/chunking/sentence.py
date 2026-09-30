import re

from app.ingestion.chunking.chunk import Chunk
from app.ingestion.document import Document


class SentenceChunker:

    def __init__(self, max_characters: int = 500):
        if max_characters <= 0:
            raise ValueError(
                "max_characters must be greater than 0"
            )

        self.max_characters = max_characters

    def chunk(self, document: Document) -> list[Chunk]:

        text = document.text.strip()

        if not text:
            return []

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text
        )

        chunks = []
        current_sentences = []
        current_length = 0
        chunk_index = 0

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            sentence_length = len(sentence)

            if (
                current_sentences
                and current_length + sentence_length + 1
                > self.max_characters
            ):
                chunk_text = " ".join(current_sentences)

                metadata = dict(document.metadata)
                metadata["chunk_index"] = chunk_index
                metadata["document_id"] = document.id
                metadata["content_hash"] = document.content_hash

                chunks.append(
                    Chunk(
                        id=f"{document.id}_chunk_{chunk_index}",
                        text=chunk_text,
                        metadata=metadata,
                    )
                )

                chunk_index += 1
                current_sentences = []
                current_length = 0

            current_sentences.append(sentence)
            current_length += sentence_length + 1

        if current_sentences:

            chunk_text = " ".join(current_sentences)

            metadata = dict(document.metadata)
            metadata["chunk_index"] = chunk_index
            metadata["document_id"] = document.id
            metadata["content_hash"] = document.content_hash

            chunks.append(
                Chunk(
                    id=f"{document.id}_chunk_{chunk_index}",
                    text=chunk_text,
                    metadata=metadata,
                )
            )

        return chunks