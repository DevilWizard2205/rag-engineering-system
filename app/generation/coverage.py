class CitationCoverage:

    def calculate(
        self,
        citations: list[int],
        number_of_sources: int,
    ) -> float:

        if number_of_sources == 0:
            return 0.0

        valid_citations = [
            citation
            for citation in citations
            if 1 <= citation <= number_of_sources
        ]

        return len(valid_citations) / number_of_sources