from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.generation.context import ContextBuilder


loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)

pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100,
)

chunks = pipeline.chunk_documents(
    documents
)


# Simulate retrieved results.
results = [
    (chunks[1], 7.38),
    (chunks[3], -1.92),
    (chunks[2], -2.87),
]


builder = ContextBuilder()

context = builder.build(results)

print("=" * 60)
print("GENERATED CONTEXT")
print("=" * 60)
print(context)