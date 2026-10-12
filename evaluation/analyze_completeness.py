
import json
from pathlib import Path


RESULTS_PATH = Path("evaluation/results/results.json")


def main():
    results = json.loads(
        RESULTS_PATH.read_text(encoding="utf-8")
    )

    failures = []

    for result in results:
        if result["should_abstain"]:
            continue

        expected = set(result["expected_sources"])
        retrieved = set(result["retrieved_sources"][:5])

        missing = expected - retrieved

        if missing:
            failures.append((result, missing))

    print("\n=== INCOMPLETE EVIDENCE ANALYSIS ===")
    print(f"Questions with missing evidence: {len(failures)}")

    for result, missing in failures:
        print("\n" + "-" * 60)
        print("ID:", result["id"])
        print("Category:", result["category"])
        print("Question:", result["question"])
        print("Expected:", result["expected_sources"])
        print("Retrieved:", result["retrieved_sources"][:5])
        print("Missing:", sorted(missing))


if __name__ == "__main__":
    main()
