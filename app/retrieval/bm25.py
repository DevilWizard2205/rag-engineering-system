import re

from rank_bm25 import BM25Okapi

from app.ingestion.chunking.chunk import Chunk


class BM25Retriever:

    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks

        self.tokenized_chunks = [
            self._tokenize(chunk.text)
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_chunks
        )

    def _tokenize(self, text: str) -> list[str]:
        return re.findall(
            r"\b\w+\b",
            text.lower()
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[tuple[Chunk, float]]:

        query_tokens = self._tokenize(query)

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        results = []

        for index in ranked_indices[:top_k]:
            results.append(
                (
                    self.chunks[index],
                    float(scores[index])
                )
            )

        return results