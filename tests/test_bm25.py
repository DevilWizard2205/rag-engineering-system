from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.retrieval.bm25 import BM25Retriever


loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)

pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100
)

chunks = pipeline.chunk_documents(
    documents
)

print("Chunks:", len(chunks))


retriever = BM25Retriever(chunks)

query = "BM25 retrieval"

results = retriever.search(
    query,
    top_k=3
)

print()
print("Query:", query)
print()

for rank, (chunk, score) in enumerate(
    results,
    start=1
):
    print(f"Result {rank}")
    print("Score:", score)
    print("Text:", chunk.text)
    print("Metadata:", chunk.metadata)
    print("-" * 60)