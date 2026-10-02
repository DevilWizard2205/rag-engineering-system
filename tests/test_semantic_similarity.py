from app.retrieval.embeddings import EmbeddingModel
from sklearn.metrics.pairwise import cosine_similarity


model = EmbeddingModel()


query = "How does RAG work?"

relevant = (
    "Retrieval Augmented Generation combines "
    "retrieval with generation."
)

irrelevant = (
    "The weather forecast predicts heavy rain tomorrow."
)


query_vector = model.embed_text(query)
relevant_vector = model.embed_text(relevant)
irrelevant_vector = model.embed_text(irrelevant)


relevant_score = cosine_similarity(
    [query_vector],
    [relevant_vector]
)[0][0]

irrelevant_score = cosine_similarity(
    [query_vector],
    [irrelevant_vector]
)[0][0]


print("Query:", query)
print()
print("Relevant similarity:", relevant_score)
print("Irrelevant similarity:", irrelevant_score)