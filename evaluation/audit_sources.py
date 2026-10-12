
import json
from pathlib import Path

from app.retrieval.vector_store import ChromaVectorStore


def main():
    results = json.loads(
        Path("evaluation/results/results.json").read_text(
            encoding="utf-8"
        )
    )

    store = ChromaVectorStore()

    for result in results:
        if result["id"] == "q002":
            continue

        expected = set(result["expected_sources"])
        retrieved = result["retrieved_sources"][:5]

        if not expected or expected.intersection(retrieved):
            continue

        ids = list(expected.union(retrieved))

        records = store.collection.get(
            ids=ids,
            include=["documents"],
        )

        texts = dict(zip(records["ids"], records["documents"]))

        print("\n" + "=" * 80)
        print(f"{result['id']}: {result['question']}")

        print("\nEXPECTED SOURCES:")
        for source_id in expected:
            print(f"\n[{source_id}]")
            print(texts.get(source_id, "NOT FOUND"))

        print("\nRETRIEVED SOURCES:")
        for rank, source_id in enumerate(retrieved, start=1):
            print(f"\nRank {rank}: [{source_id}]")
            print(texts.get(source_id, "NOT FOUND"))


if __name__ == "__main__":
    main()
