import json
from pathlib import Path


RESULTS_PATH = Path("evaluation/results/results.json")


def main():
    with RESULTS_PATH.open("r", encoding="utf-8") as file:
        results = json.load(file)

    print("\n=== RETRIEVAL FAILURE ANALYSIS ===\n")

    failures = []

    for result in results:
        expected_sources = set(result["expected_sources"])
        retrieved_sources = result["retrieved_sources"]

        # Skip questions that intentionally have no expected sources.
        if not expected_sources:
            continue

        retrieved_top_5 = set(retrieved_sources[:5])

        if not expected_sources.intersection(retrieved_top_5):
            failures.append(result)

    print(f"Total answerable questions: "
          f"{sum(bool(r['expected_sources']) for r in results)}")

    print(f"Questions with no expected source in Top-5: {len(failures)}")

    print("\n--- FAILURES ---\n")

    for result in failures:
        print(f"ID: {result['id']}")
        print(f"Question: {result['question']}")
        print(f"Expected sources: {result['expected_sources']}")
        print(f"Retrieved sources: {result['retrieved_sources']}")
        print(f"Confidence: {result['confidence']:.4f}")
        print("-" * 70)


if __name__ == "__main__":
    main()
    