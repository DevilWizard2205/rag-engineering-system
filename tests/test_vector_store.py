from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore


loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.md"
)

pipeline = ChunkingPipeline(
    strategy="recursive",
    chunk_size=100
)

chunks = pipeline.chunk_documents(documents)

print("Chunks:", len(chunks))


embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk.text for chunk in chunks]
)

print("Embeddings:", len(embeddings))
print("Vector dimensions:", len(embeddings[0]))


vector_store = ChromaVectorStore(
    collection_name="test_collection"
)

vector_store.add_chunks(
    chunks,
    embeddings
)

query = "How does the system perform retrieval?"

query_embedding = embedding_model.embed_text(
    query
)

results = vector_store.search(
    query_embedding,
    top_k=3
)

print()
print("Query:", query)
print()

for i, text in enumerate(results["documents"][0]):
    print(f"Result {i + 1}:")
    print(text)
    print("Metadata:", results["metadatas"][0][i])
    print("-" * 60)