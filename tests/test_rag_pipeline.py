from app.ingestion.loader import DocumentLoader
from app.ingestion.chunking.pipeline import ChunkingPipeline

from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore
from app.retrieval.hybrid import HybridRetriever

from app.generation.mock_llm import MockLLM
from app.generation.pipeline import RAGPipeline


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
# Embeddings
# -------------------------
embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk.text for chunk in chunks]
)


# -------------------------
# Vector store
# -------------------------
vector_store = ChromaVectorStore(
    collection_name="rag_pipeline_final_test"
)

vector_store.add_chunks(
    chunks,
    embeddings,
)


# -------------------------
# Hybrid retriever
# -------------------------
retriever = HybridRetriever(
    chunks=chunks,
    vector_store=vector_store,
    embedding_model=embedding_model,
)


# -------------------------
# Mock LLM
# -------------------------
llm = MockLLM()


# -------------------------
# RAG pipeline
# -------------------------
rag = RAGPipeline(
    retriever=retriever,
    llm=llm,
    retrieval_top_k=4,
    final_top_k=3,
    confidence_threshold=0.5,
)


# -------------------------
# Ask question
# -------------------------
query = "How does the system perform retrieval?"

result = rag.ask(query)


# -------------------------
# Display result
# -------------------------
print("=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])

print()
print("=" * 60)
print("CITATIONS")
print("=" * 60)

print(result["citations"])

print()
print("=" * 60)
print("CITATION VALIDATION")
print("=" * 60)

print(result["citation_validation"])

print()
print("=" * 60)
print("CITATION COVERAGE")
print("=" * 60)

print(result["citation_coverage"])

print()
print("=" * 60)
print("RETRIEVAL CONFIDENCE")
print("=" * 60)

print(result["retrieval_confidence"])

print()
print("=" * 60)
print("COMPOSITE CONFIDENCE")
print("=" * 60)

print(result["confidence"])

print()
print("=" * 60)
print("ABSTAINED")
print("=" * 60)

print(result["abstained"])