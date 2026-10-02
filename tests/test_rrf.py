from app.retrieval.rrf import ReciprocalRankFusion


rrf = ReciprocalRankFusion(k=60)

bm25_ranking = [
    "chunk_1",
    "chunk_2",
    "chunk_3",
]

dense_ranking = [
    "chunk_1",
    "chunk_3",
    "chunk_2",
]

results = rrf.fuse(
    ranked_lists=[
        bm25_ranking,
        dense_ranking,
    ],
    top_k=3,
)

print("=" * 60)
print("RRF RESULTS")
print("=" * 60)

for rank, (document_id, score) in enumerate(results, start=1):
    print(
        f"{rank}. {document_id} "
        f"RRF Score={score:.6f}"
    )