from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline


loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)


pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100
)

chunks = pipeline.chunk_documents(documents)


print("Documents:", len(documents))
print("Chunks:", len(chunks))
print()

for chunk in chunks:
    print("ID:", chunk.id)
    print("Text:", chunk.text)
    print("Metadata:", chunk.metadata)
    print("-" * 60)