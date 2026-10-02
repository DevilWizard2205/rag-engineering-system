class CitationValidator:

    def validate(
        self,
        citations: list[int],
        number_of_sources: int,
    ) -> dict:

        valid = [
            citation
            for citation in citations
            if 1 <= citation <= number_of_sources
        ]

        invalid = [
            citation
            for citation in citations
            if citation < 1
            or citation > number_of_sources
        ]

        all_valid = (
            len(citations) > 0
            and len(invalid) == 0
        )

        return {
            "citations": citations,
            "valid_citations": valid,
            "invalid_citations": invalid,
            "all_valid": all_valid,
        }