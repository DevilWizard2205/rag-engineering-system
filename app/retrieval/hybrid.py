from app.retrieval.bm25 import BM25Retriever
from app.retrieval.rrf import ReciprocalRankFusion
from app.retrieval.reranker import CrossEncoderReranker


class HybridRetriever:
    def __init__(
        self,
        chunks,
        vector_store,
        embedding_model,
        rrf_k: int = 60,
        reranker_model: str = (
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        ),
    ):
        self.chunks = chunks
        self.vector_store = vector_store
        self.embedding_model = embedding_model

        self.bm25 = BM25Retriever(chunks)

        self.rrf = ReciprocalRankFusion(
            k=rrf_k
        )

        self.reranker = CrossEncoderReranker(
            model_name=reranker_model
        )

    def search(
        self,
        query: str,
        retrieval_top_k: int = 10,
        final_top_k: int = 5,
    ):
        # -------------------------
        # BM25 retrieval
        # -------------------------
        bm25_results = self.bm25.search(
            query,
            top_k=retrieval_top_k,
        )

        bm25_ranking = [
            chunk.id
            for chunk, score in bm25_results
        ]

        # -------------------------
        # Dense retrieval
        # -------------------------
        query_embedding = (
            self.embedding_model.embed_text(query)
        )

        dense_results = self.vector_store.search(
            query_embedding,
            top_k=retrieval_top_k,
        )

        dense_ranking = [
            metadata["document_id"]
            + "_chunk_"
            + str(metadata["chunk_index"])
            for metadata in dense_results["metadatas"][0]
        ]

        # -------------------------
        # RRF fusion
        # -------------------------
        fused_results = self.rrf.fuse(
            ranked_lists=[
                bm25_ranking,
                dense_ranking,
            ],
            top_k=retrieval_top_k,
        )

        # -------------------------
        # Convert IDs back to chunks
        # -------------------------
        chunk_lookup = {
            chunk.id: chunk
            for chunk in self.chunks
        }

        candidate_chunks = [
            chunk_lookup[chunk_id]
            for chunk_id, score in fused_results
        ]

        # -------------------------
        # Cross-encoder reranking
        # -------------------------
        reranked_results = self.reranker.rerank(
            query=query,
            chunks=candidate_chunks,
            top_k=final_top_k,
        )

        return reranked_results