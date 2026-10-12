from app.generation.nemotron_llm import NemotronLLM
from app.generation.pipeline import RAGPipeline
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore
from app.retrieval.hybrid import HybridRetriever


def main():
    embedding_model = EmbeddingModel()

    vector_store = ChromaVectorStore()

    retriever = HybridRetriever(
        vector_store=vector_store,
        embedding_model=embedding_model,
    )

    llm = NemotronLLM()

    pipeline = RAGPipeline(
        retriever=retriever,
        llm=llm,
        retrieval_top_k=10,
        final_top_k=5,
    )

    result = pipeline.ask(
        "What is hybrid retrieval?"
    )

    print("\n=== ANSWER ===")
    print(result["answer"])

    print("\n=== CITATIONS ===")
    print(result["citations"])

    print("\n=== CITATION VALIDATION ===")
    print(result["citation_validation"])

    print("\n=== CITATION COVERAGE ===")
    print(result["citation_coverage"])

    print("\n=== RETRIEVAL CONFIDENCE ===")
    print(result["retrieval_confidence"])

    print("\n=== COMPOSITE CONFIDENCE ===")
    print(result["confidence"])

    print("\n=== ABSTAINED ===")
    print(result["abstained"])

    print("\n=== SOURCES ===")
    for chunk, score in result["results"]:
        print(f"{chunk.id} | score={score:.4f}")


if __name__ == "__main__":
    main()