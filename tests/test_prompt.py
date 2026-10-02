from app.generation.prompt import PromptBuilder


builder = PromptBuilder()

context = """
[1]
The system uses dense retrieval and BM25 retrieval.

[2]
Reciprocal Rank Fusion combines results from different
retrieval systems.
"""

query = "How does the system perform retrieval?"

prompt = builder.build(
    query=query,
    context=context,
)

print("=" * 60)
print("GENERATED PROMPT")
print("=" * 60)
print(prompt)