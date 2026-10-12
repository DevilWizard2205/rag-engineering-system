import json
from pathlib import Path


RESULTS_PATH = Path("evaluation/results/results.json")
METRICS_PATH = Path("evaluation/results/metrics.json")


def hit_at_k(expected_sources, retrieved_sources, k):
    """
    Returns 1 if at least one expected source appears
    in the top-k retrieved sources.
    """
    if not expected_sources:
        return None

    retrieved_top_k = retrieved_sources[:k]

    return int(
        any(source in retrieved_top_k for source in expected_sources)
    )
def expected_source_recall_at_k(expected_sources, retrieved_sources, k):
    if not expected_sources:
        return None

    retrieved_top_k = set(retrieved_sources[:k])
    matched_sources = set(expected_sources).intersection(retrieved_top_k)

    return len(matched_sources) / len(expected_sources)

def all_sources_hit_at_k(expected_sources, retrieved_sources, k):
    if not expected_sources:
        return None

    expected = set(expected_sources)
    retrieved = set(retrieved_sources[:k])

    return int(expected.issubset(retrieved))

def citation_source_ids(citations, retrieved_sources):
    """
    Convert citation numbers such as [1, 3]
    into the corresponding chunk IDs.
    """
    source_ids = []

    for citation in citations:
        index = citation - 1

        if 0 <= index < len(retrieved_sources):
            source_ids.append(retrieved_sources[index])

    return source_ids


def calculate_metrics(results):
    answerable = [
        result
        for result in results
        if not result["should_abstain"]
    ]

    abstention_cases = [
        result
        for result in results
        if result["should_abstain"]
    ]

    metrics = {
        "total_questions": len(results),
        "categories": {},
        "retrieval": {},
        "citations": {},
        "abstention": {},
        "confidence": {},
    }

    # --------------------------------------------------
    # Category counts
    # --------------------------------------------------

    for result in results:
        category = result["category"]

        if category not in metrics["categories"]:
            metrics["categories"][category] = 0

        metrics["categories"][category] += 1

    # --------------------------------------------------
    # Retrieval metrics
    # --------------------------------------------------

    
    for k in [1, 3, 5]:
        hits = []
        recalls = []
        complete_hits = []

        for result in answerable:
            expected_sources = result["expected_sources"]
            retrieved_sources = result["retrieved_sources"]

            hit = hit_at_k(
                expected_sources,
                retrieved_sources,
                k,
            )

            recall = expected_source_recall_at_k(
                expected_sources,
                retrieved_sources,
                k,
            )

            complete = all_sources_hit_at_k(
                expected_sources,
                retrieved_sources,
                k,
            )

            if hit is not None:
                hits.append(hit)

            if recall is not None:
                recalls.append(recall)

            if complete is not None:
                complete_hits.append(complete)

        metrics["retrieval"][f"hit_at_{k}"] = (
            sum(hits) / len(hits) if hits else None
        )

        metrics["retrieval"][f"expected_source_recall_at_{k}"] = (
            sum(recalls) / len(recalls) if recalls else None
        )

        metrics["retrieval"][f"all_sources_hit_at_{k}"] = (
            sum(complete_hits) / len(complete_hits)
            if complete_hits else None
        )

    # --------------------------------------------------
    # Citation metrics
    # --------------------------------------------------

    citation_validity = []
    citation_coverage = []
    citation_accuracy = []

    for result in results:
        validation = result["citation_validation"]

        citation_validity.append(
            int(validation["all_valid"])
        )

        citation_coverage.append(
            result["citation_coverage"]
        )

        expected_sources = set(
            result["expected_sources"]
        )

        retrieved_sources = result["retrieved_sources"]

        cited_sources = set(
            citation_source_ids(
                result["citations"],
                retrieved_sources,
            )
        )

        if expected_sources and cited_sources:
            citation_accuracy.append(
                int(
                    bool(
                        expected_sources
                        & cited_sources
                    )
                )
            )

    metrics["citations"]["validity_rate"] = (
        sum(citation_validity)
        / len(citation_validity)
        if citation_validity
        else None
    )

    metrics["citations"]["mean_coverage"] = (
        sum(citation_coverage)
        / len(citation_coverage)
        if citation_coverage
        else None
    )

    metrics["citations"]["expected_source_citation_rate"] = (
        sum(citation_accuracy)
        / len(citation_accuracy)
        if citation_accuracy
        else None
    )

    # --------------------------------------------------
    # Abstention metrics
    # --------------------------------------------------

    correct_abstentions = sum(
        int(result["abstained"])
        for result in abstention_cases
    )

    missed_abstentions = len(abstention_cases) - correct_abstentions

    false_abstentions = sum(
        int(result["abstained"])
        for result in answerable
    )

    correct_answers = sum(
        int(not result["abstained"])
        for result in answerable
    )

    metrics["abstention"]["expected_abstentions"] = len(
        abstention_cases
    )

    metrics["abstention"]["correct_abstentions"] = (
        correct_abstentions
    )

    metrics["abstention"]["missed_abstentions"] = (
        missed_abstentions
    )

    metrics["abstention"]["false_abstentions"] = (
        false_abstentions
    )

    metrics["abstention"]["correct_non_abstentions"] = (
        correct_answers
    )

    metrics["abstention"]["abstention_accuracy"] = (
        (
            correct_abstentions
            + correct_answers
        )
        / len(results)
        if results
        else None
    )

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    confidence_values = [
        result["confidence"]
        for result in results
    ]

    metrics["confidence"]["mean"] = (
        sum(confidence_values)
        / len(confidence_values)
        if confidence_values
        else None
    )

    metrics["confidence"]["mean_by_category"] = {}

    categories = set(
        result["category"]
        for result in results
    )

    for category in categories:
        category_values = [
            result["confidence"]
            for result in results
            if result["category"] == category
        ]

        metrics["confidence"]["mean_by_category"][category] = (
            sum(category_values)
            / len(category_values)
        )

    return metrics


def main():
    with RESULTS_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        results = json.load(file)

    metrics = calculate_metrics(results)

    METRICS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with METRICS_PATH.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            metrics,
            file,
            indent=2,
        )

    print("\n=== RAG EVALUATION METRICS ===")
    print(
        f"Total questions: "
        f"{metrics['total_questions']}"
    )

    print("\nRetrieval:")
    for key, value in metrics["retrieval"].items():
        print(f"  {key}: {value:.4f}")

    print("\nCitations:")
    for key, value in metrics["citations"].items():
        print(f"  {key}: {value:.4f}")

    print("\nAbstention:")
    for key, value in metrics["abstention"].items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")

    print("\nConfidence:")
    print(
        f"  mean: "
        f"{metrics['confidence']['mean']:.4f}"
    )

    print("\nMean confidence by category:")
    for category, value in metrics["confidence"][
        "mean_by_category"
    ].items():
        print(
            f"  {category}: {value:.4f}"
        )

    print(
        f"\nMetrics saved to: {METRICS_PATH}"
    )


if __name__ == "__main__":
    main()