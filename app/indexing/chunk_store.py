from app.ingestion.chunking.chunk import Chunk
from app.retrieval.vector_store import ChromaVectorStore


class IndexedChunkStore:

    def __init__(self, vector_store: ChromaVectorStore):
        self.vector_store = vector_store

    def load_chunks(self) -> list[Chunk]:
        data = self.vector_store.collection.get()

        chunks = []

        for chunk_id, text, metadata in zip(
            data["ids"],
            data["documents"],
            data["metadatas"],
        ):
            chunks.append(
                Chunk(
                    id=chunk_id,
                    text=text,
                    metadata=metadata,
                )
            )

        return chunks