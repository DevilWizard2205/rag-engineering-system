from collections import defaultdict


class ReciprocalRankFusion:
    def __init__(self, k: int = 60):
        self.k = k

    def fuse(self, ranked_lists: list[list[str]], top_k: int = 5):
        scores = defaultdict(float)

        for ranked_list in ranked_lists:
            for rank, document_id in enumerate(ranked_list, start=1):
                scores[document_id] += 1 / (self.k + rank)

        ranked_results = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return ranked_results[:top_k]