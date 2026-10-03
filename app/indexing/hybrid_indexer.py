from app.ingestion.chunking.chunk import Chunk
from app.indexing.indexer import Indexer
from app.retrieval.bm25 import BM25Retriever


class HybridIndexer:
    def __init__(self, dense_indexer: Indexer):
        self.dense_indexer = dense_indexer
        self.bm25_retriever: BM25Retriever | None = None

    def index_chunks(self, chunks: list[Chunk]) -> None:
        if not chunks:
            return

        # Build the dense vector index.
        self.dense_indexer.index_chunks(chunks)

        # Build the sparse BM25 index.
        self.bm25_retriever = BM25Retriever(chunks)

    def get_bm25_retriever(self) -> BM25Retriever:
        if self.bm25_retriever is None:
            raise RuntimeError("BM25 index has not been built yet.")

        return self.bm25_retriever