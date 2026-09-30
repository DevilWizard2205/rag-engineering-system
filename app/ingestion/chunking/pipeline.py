from app.ingestion.chunking.factory import get_chunker
from app.ingestion.document import Document
from app.ingestion.chunking.chunk import Chunk


class ChunkingPipeline:

    def __init__(self, strategy: str, **kwargs):
        self.chunker = get_chunker(
            strategy,
            **kwargs
        )

    def chunk_documents(
        self,
        documents: list[Document]
    ) -> list[Chunk]:

        chunks = []

        for document in documents:
            document_chunks = self.chunker.chunk(document)
            chunks.extend(document_chunks)

        return chunks