from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.retrieval.reranker import CrossEncoderReranker


# -------------------------
# Load documents
# -------------------------
loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)


# -------------------------
# Chunk documents
# -------------------------
pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100,
)

chunks = pipeline.chunk_documents(
    documents
)


# -------------------------
# Create reranker
# -------------------------
reranker = CrossEncoderReranker()


# -------------------------
# Rerank
# -------------------------
query = "How does retrieval work?"

results = reranker.rerank(
    query=query,
    chunks=chunks,
    top_k=3,
)


# -------------------------
# Display results
# -------------------------
print("=" * 60)
print("CROSS-ENCODER RERANKING")
print("=" * 60)

for rank, (chunk, score) in enumerate(
    results,
    start=1,
):
    print(
        f"{rank}. Score={score:.4f} "
        f"Chunk={chunk.id}"
    )

    print(chunk.text)
    print()