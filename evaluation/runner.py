import json
from pathlib import Path

from app.generation.nemotron_llm import NemotronLLM
from app.generation.pipeline import RAGPipeline
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.hybrid import HybridRetriever
from app.retrieval.vector_store import ChromaVectorStore


QUESTIONS_PATH = Path("evaluation/golden_questions.json")
RESULTS_DIRECTORY = Path("evaluation/results")
RESULTS_PATH = RESULTS_DIRECTORY / "results.json"


def load_questions():
    with QUESTIONS_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_pipeline():
    embedding_model = EmbeddingModel()

    vector_store = ChromaVectorStore()

    retriever = HybridRetriever(
        vector_store=vector_store,
        embedding_model=embedding_model,
        reranker_model="cross-encoder/ms-marco-MiniLM-L-6-v2",
    )

    llm = NemotronLLM()

    return RAGPipeline(
        retriever=retriever,
        llm=llm,
        retrieval_top_k=10,
        final_top_k=5,
    )


def run_evaluation():
    questions = load_questions()
    pipeline = build_pipeline()

    RESULTS_DIRECTORY.mkdir(parents=True, exist_ok=True)

    results = []

    total = len(questions)

    for index, question in enumerate(questions, start=1):
        print(f"[{index}/{total}] {question['id']}: {question['question']}")

        result = pipeline.ask(question["question"])

        retrieved_sources = [
            chunk.id
            for chunk, score in result["results"]
        ]

        evaluation_result = {
            "id": question["id"],
            "question": question["question"],
            "category": question["category"],
            "expected_answer": question["expected_answer"],
            "expected_sources": question["expected_sources"],
            "should_abstain": question["should_abstain"],
            "generated_answer": result["answer"],
            "retrieved_sources": retrieved_sources,
            "citations": result["citations"],
            "citation_validation": result["citation_validation"],
            "citation_coverage": result["citation_coverage"],
            "retrieval_confidence": result["retrieval_confidence"],
            "confidence": result["confidence"],
            "abstained": result["abstained"],
        }

        results.append(evaluation_result)

        print(
            f"    citations={result['citations']} "
            f"confidence={result['confidence']:.4f} "
            f"abstained={result['abstained']}"
        )

    with RESULTS_PATH.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print()
    print(f"Evaluation complete: {total} questions")
    print(f"Results saved to: {RESULTS_PATH}")


if __name__ == "__main__":
    run_evaluation()