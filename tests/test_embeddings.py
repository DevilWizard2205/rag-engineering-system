from app.retrieval.embeddings import EmbeddingModel


model = EmbeddingModel()

text = "Retrieval Augmented Generation combines retrieval with generation."

vector = model.embed_text(text)

print("Vector type:", type(vector))
print("Vector dimensions:", len(vector))
print("First 10 values:", vector[:10])