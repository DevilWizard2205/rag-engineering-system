from app.generation.nemotron_llm import NemotronLLM


def main():
    llm = NemotronLLM()

    prompt = """
You are a helpful assistant.

Answer the following question in one or two sentences:

What is hybrid retrieval in a RAG system?
"""

    answer = llm.generate(prompt)

    print("\nNemotron response:")
    print(answer)


if __name__ == "__main__":
    main()