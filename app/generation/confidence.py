class ConfidenceCalculator:

    def retrieval_confidence(
        self,
        results,
    ) -> float:

        if not results:
            return 0.0

        scores = [
            score
            for chunk, score in results
        ]

        top_score = max(scores)

        confidence = 1 / (
            1 + pow(2.71828, -top_score)
        )

        return round(
            confidence,
            4,
        )

    def composite_confidence(
        self,
        retrieval_confidence: float,
        citation_valid: bool,
        citation_coverage: float,
    ) -> float:

        citation_validity = (
            1.0
            if citation_valid
            else 0.0
        )

        confidence = (
            0.5 * retrieval_confidence
            + 0.2 * citation_validity
            + 0.3 * citation_coverage
        )

        return round(
            confidence,
            4,
        )