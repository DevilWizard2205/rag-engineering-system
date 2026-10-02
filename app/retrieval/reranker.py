from sentence_transformers import CrossEncoder


class CrossEncoderReranker:
    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        chunks,
        top_k: int = 5,
    ):
        if not chunks:
            return []

        pairs = [
            [query, chunk.text]
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        ranked_results = sorted(
            zip(chunks, scores),
            key=lambda item: float(item[1]),
            reverse=True,
        )

        return [
            (chunk, float(score))
            for chunk, score in ranked_results[:top_k]
        ]