class AbstentionChecker:

    def __init__(
        self,
        threshold: float = 0.5,
    ):
        self.threshold = threshold

    def should_abstain(
        self,
        confidence: float,
    ) -> bool:

        return confidence < self.threshold

    def get_message(self) -> str:
        return (
            "I don't have enough information "
            "in the provided documents to answer "
            "this question."
        )