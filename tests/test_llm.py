from app.generation.mock_llm import MockLLM


llm = MockLLM()

prompt = """
Answer the question using the provided context.

Question:
How does retrieval work?

Context:
[1]
The system uses dense retrieval and BM25 retrieval.
"""

answer = llm.generate(prompt)

print("=" * 60)
print("LLM RESPONSE")
print("=" * 60)
print(answer)