class PromptBuilder:

    def build(
        self,
        query: str,
        context: str,
    ) -> str:

        return f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information
to answer the question, say:
"I don't have enough information in the provided documents."

Do not use outside knowledge.

Cite the relevant context sources using their numbers,
for example [1] or [2].

User question:
{query}

Context:
{context}

Answer:
""".strip()