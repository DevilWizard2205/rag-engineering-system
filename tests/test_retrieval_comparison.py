from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore
from app.retrieval.bm25 import BM25Retriever


# -------------------------
# Load and chunk documents
# -------------------------

loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)

pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100
)

chunks = pipeline.chunk_documents(documents)


# -------------------------
# Create BM25 retriever
# -------------------------

bm25 = BM25Retriever(chunks)


# -------------------------
# Create dense retriever
# -------------------------

embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk.text for chunk in chunks]
)

vector_store = ChromaVectorStore(
    collection_name="comparison_collection"
)

vector_store.add_chunks(
    chunks,
    embeddings
)


# -------------------------
# Query
# -------------------------

query = "BM25 retrieval"


# -------------------------
# BM25 search
# -------------------------

bm25_results = bm25.search(
    query,
    top_k=3
)


print("=" * 60)
print("BM25 RESULTS")
print("=" * 60)

for rank, (chunk, score) in enumerate(
    bm25_results,
    start=1
):
    print(
        f"{rank}. Score={score:.4f} "
        f"Chunk={chunk.id}"
    )
    print(chunk.text)
    print()


# -------------------------
# Dense search
# -------------------------

query_embedding = embedding_model.embed_text(
    query
)

dense_results = vector_store.search(
    query_embedding,
    top_k=3
)


print("=" * 60)
print("DENSE RESULTS")
print("=" * 60)

for rank, text in enumerate(
    dense_results["documents"][0],
    start=1
):
    metadata = dense_results["metadatas"][0][rank - 1]

    print(
        f"{rank}. Chunk={metadata['document_id']}"
        f"_chunk_{metadata['chunk_index']}"
    )
    print(text)
    print()