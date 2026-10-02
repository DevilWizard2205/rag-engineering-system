from app.generation.confidence import ConfidenceCalculator


calculator = ConfidenceCalculator()


results = [
    ("chunk_1", 7.38),
    ("chunk_2", -8.59),
    ("chunk_3", -9.46),
]


retrieval_confidence = (
    calculator.retrieval_confidence(
        results
    )
)


composite = (
    calculator.composite_confidence(
        retrieval_confidence=retrieval_confidence,
        citation_valid=True,
        citation_coverage=0.667,
    )
)


print("=" * 60)
print("RETRIEVAL CONFIDENCE")
print("=" * 60)

print(retrieval_confidence)


print()
print("=" * 60)
print("COMPOSITE CONFIDENCE")
print("=" * 60)

print(composite)