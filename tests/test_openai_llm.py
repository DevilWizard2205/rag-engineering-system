from app.generation.openai_llm import OpenAILLM


llm = OpenAILLM()

prompt = """
Answer the question using only the context.

Context:
[1]
The system uses dense retrieval and BM25 retrieval.

Question:
How does the system perform retrieval?

Cite the source using [1].
"""

answer = llm.generate(prompt)

print("=" * 60)
print("OPENAI LLM RESPONSE")
print("=" * 60)
print(answer)