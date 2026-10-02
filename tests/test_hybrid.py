from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore
from app.retrieval.hybrid import HybridRetriever


# -------------------------
# Load documents
# -------------------------
loader = DocumentLoader()
documents = loader.load("data/raw/sample.md")


# -------------------------
# Chunk documents
# -------------------------
pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100,
)

chunks = pipeline.chunk_documents(documents)


# -------------------------
# Create embeddings
# -------------------------
embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk.text for chunk in chunks]
)


# -------------------------
# Create vector store
# -------------------------
vector_store = ChromaVectorStore(
    collection_name="hybrid_test_collection"
)

vector_store.add_chunks(
    chunks,
    embeddings,
)


# -------------------------
# Create hybrid retriever
# -------------------------
retriever = HybridRetriever(
    chunks=chunks,
    vector_store=vector_store,
    embedding_model=embedding_model,
)


# -------------------------
# Search
# -------------------------
query = "BM25 retrieval"

results = retriever.search(
    query=query,
    retrieval_top_k=4,
    final_top_k=3,
)


# -------------------------
# Display results
# -------------------------
print("=" * 60)
print("HYBRID RRF RESULTS")
print("=" * 60)

for rank, (chunk, score) in enumerate(results, start=1):
    print(
        f"{rank}. Reranker Score={score:.6f} "
        f"Chunk={chunk.id}"
    )
    print(chunk.text)
    print()