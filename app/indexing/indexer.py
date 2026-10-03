from app.ingestion.chunking.chunk import Chunk
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore


class Indexer:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: ChromaVectorStore,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def index_chunks(self, chunks: list[Chunk]) -> None:
        if not chunks:
            return

        texts = [chunk.text for chunk in chunks]

        embeddings = self.embedding_model.embed_documents(texts)

        self.vector_store.add_chunks(
            chunks=chunks,
            embeddings=embeddings,
        )