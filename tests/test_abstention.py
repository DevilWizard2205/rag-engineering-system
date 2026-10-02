from app.generation.abstention import AbstentionChecker


checker = AbstentionChecker(
    threshold=0.5
)


test_scores = [
    0.90,
    0.50,
    0.32,
]


for score in test_scores:

    abstain = checker.should_abstain(
        confidence=score
    )

    print(
        f"Confidence={score:.2f} "
        f"Abstain={abstain}"
    )

    if abstain:
        print(
            checker.get_message()
        )

    print()