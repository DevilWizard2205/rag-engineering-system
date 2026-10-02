from app.generation.llm import LLM


class MockLLM(LLM):

    def generate(self, prompt: str) -> str:
        return (
            "The system performs retrieval using dense "
            "retrieval and BM25 retrieval [1]. "
            "Reciprocal Rank Fusion combines results "
            "from the different retrieval systems [3]."
        )