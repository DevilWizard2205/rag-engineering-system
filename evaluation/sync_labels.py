
import json
from pathlib import Path

GOLDEN_PATH = Path("evaluation/golden_questions.json")
RESULTS_PATH = Path("evaluation/results/results.json")


def main():
    golden = json.loads(GOLDEN_PATH.read_text(encoding="utf-8"))
    results = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))

    golden_lookup = {question["id"]: question for question in golden}

    changes = 0

    for result in results:
        question_id = result["id"]

        if question_id not in golden_lookup:
            raise ValueError(f"Missing golden question: {question_id}")

        gold = golden_lookup[question_id]

        if result["expected_sources"] != gold["expected_sources"]:
            print(f"\n{question_id}")
            print(f"  Old: {result['expected_sources']}")
            print(f"  New: {gold['expected_sources']}")
            changes += 1

        result["expected_sources"] = gold["expected_sources"]
        result["should_abstain"] = gold["should_abstain"]
        result["expected_answer"] = gold["expected_answer"]

    backup_path = RESULTS_PATH.with_name("results_before_label_sync.json")

    if not backup_path.exists():
        backup_path.write_text(
            RESULTS_PATH.read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    RESULTS_PATH.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\nSynchronized {changes} changed source labels.")
    print(f"Backup: {backup_path}")


if __name__ == "__main__":
    main()
