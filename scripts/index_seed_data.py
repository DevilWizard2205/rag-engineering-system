from pathlib import Path

from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.factory import get_chunker
from app.indexing.indexer import Indexer
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore


SEED_DIRECTORY = Path("data/raw/seed")


def main():
    loader = DocumentLoader()
    chunker = get_chunker("recursive", chunk_size=500)

    embedding_model = EmbeddingModel()
    vector_store = ChromaVectorStore()

    indexer = Indexer(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    documents = []

    for file_path in sorted(SEED_DIRECTORY.iterdir()):
        if file_path.is_file():
            loaded_documents = loader.load(str(file_path))
            documents.extend(loaded_documents)

    print(f"Loaded documents: {len(documents)}")

    chunks = []

    for document in documents:
        document_chunks = chunker.chunk(document)
        chunks.extend(document_chunks)

    print(f"Generated chunks: {len(chunks)}")

    indexer.index_chunks(chunks)

    print("Dense indexing complete.")


if __name__ == "__main__":
    main()