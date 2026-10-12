
import json
from pathlib import Path

from app.retrieval.vector_store import ChromaVectorStore


RESULTS_PATH = Path("evaluation/results/results.json")
OUTPUT_PATH = Path("evaluation/results/completeness_audit.txt")


def main():
    results = json.loads(
        RESULTS_PATH.read_text(encoding="utf-8")
    )

    store = ChromaVectorStore()
    data = store.collection.get(
        include=["documents", "metadatas"]
    )

    chunk_lookup = dict(
        zip(data["ids"], data["documents"])
    )

    lines = []

    for result in results:
        if result["should_abstain"]:
            continue

        expected = set(result["expected_sources"])
        retrieved = result["retrieved_sources"][:5]
        missing = expected - set(retrieved)

        if not missing:
            continue

        lines.append("=" * 75)
        lines.append(f"ID: {result['id']}")
        lines.append(f"Question: {result['question']}")
        lines.append(f"Expected answer: {result['expected_answer']}")

        lines.append("\nEXPECTED CHUNKS:")

        for chunk_id in result["expected_sources"]:
            lines.append(f"\n[{chunk_id}]")
            lines.append(
                chunk_lookup.get(chunk_id, "CHUNK NOT FOUND")
            )

        lines.append("\nRETRIEVED TOP-5:")

        for rank, chunk_id in enumerate(retrieved, 1):
            lines.append(f"\nRank {rank}: [{chunk_id}]")
            lines.append(
                chunk_lookup.get(chunk_id, "CHUNK NOT FOUND")
            )

        lines.append("\n")

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(f"Audit saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
