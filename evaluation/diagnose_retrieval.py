
import json
from pathlib import Path

from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import ChromaVectorStore
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.rrf import ReciprocalRankFusion
from app.indexing.chunk_store import IndexedChunkStore
from app.retrieval.reranker import CrossEncoderReranker


def main():
    questions = json.loads(
        Path("evaluation/golden_questions.json").read_text(encoding="utf-8")
    )

    vector_store = ChromaVectorStore()
    embedding_model = EmbeddingModel()
    chunks = IndexedChunkStore(vector_store).load_chunks()

    bm25 = BM25Retriever(chunks)
    rrf = ReciprocalRankFusion(k=60)
    reranker = CrossEncoderReranker()
    chunk_lookup = {chunk.id: chunk for chunk in chunks}
    stages = {
            "bm25": [],
            "dense": [],
            "fusion": [],
            "fusion_top5": [],
            "reranked_top5": [],
            "dense_top5": [],
        }

    for question in questions:
        expected = set(question["expected_sources"])

        if not expected:
            continue

        query = question["question"]

        bm25_ids = [
            chunk.id
            for chunk, score in bm25.search(query, top_k=10)
        ]

        embedding = embedding_model.embed_text(query)
        dense_ids = vector_store.search(
            embedding, top_k=10
        )["ids"][0]

        fused_ids = [
            chunk_id
            for chunk_id, score in rrf.fuse(
                [bm25_ids, dense_ids], top_k=20
            )
        ]
        candidate_chunks = [
            chunk_lookup[chunk_id]
            for chunk_id in fused_ids
            if chunk_id in chunk_lookup
        ]

        reranked_ids = [
            chunk.id
            for chunk, score in reranker.rerank(
                query=query,
                chunks=candidate_chunks,
                top_k=5,
            )
        ]
        for name, ids in [
            ("bm25", bm25_ids),
            ("dense", dense_ids),
            ("fusion", fused_ids),
            ("fusion_top5", fused_ids[:5]),
            ("reranked_top5", reranked_ids),
            ("dense_top5", dense_ids[:5]),
        ]:
            recall = len(expected.intersection(ids)) / len(expected)
            stages[name].append(recall)

    print("\n=== RETRIEVAL STAGE DIAGNOSTICS ===")

    for name, recalls in stages.items():
        average = sum(recalls) / len(recalls)
        print(f"{name:10s} Recall@10: {average:.4f}")


if __name__ == "__main__":
    main()
