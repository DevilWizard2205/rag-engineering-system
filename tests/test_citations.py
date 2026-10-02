from app.generation.citations import CitationExtractor
from app.generation.citation_validator import CitationValidator


answer = (
    "The system uses dense retrieval [1] "
    "and BM25 retrieval [2]. "
    "RRF combines the results [4]."
)


extractor = CitationExtractor()

citations = extractor.extract(answer)

print("=" * 60)
print("EXTRACTED CITATIONS")
print("=" * 60)

print(citations)


validator = CitationValidator()

result = validator.validate(
    citations=citations,
    number_of_sources=3,
)

print()
print("=" * 60)
print("VALIDATION")
print("=" * 60)

print(result)