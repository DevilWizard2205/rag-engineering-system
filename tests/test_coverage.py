from app.generation.coverage import CitationCoverage


coverage = CitationCoverage()


test_cases = [
    ([1, 2], 3),
    ([1, 2, 3], 3),
    ([], 3),
    ([1, 5], 3),
]


for citations, number_of_sources in test_cases:

    score = coverage.calculate(
        citations=citations,
        number_of_sources=number_of_sources,
    )

    print(
        f"Citations={citations} "
        f"Sources={number_of_sources} "
        f"Coverage={score:.3f}"
    )