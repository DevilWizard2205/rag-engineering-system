from app.ingestion.chunking.factory import get_chunker


fixed = get_chunker(
    "fixed",
    chunk_size=100,
    overlap=20
)

sentence = get_chunker(
    "sentence",
    max_characters=100
)

recursive = get_chunker(
    "recursive",
    chunk_size=100
)


print("Fixed:", type(fixed).__name__)
print("Sentence:", type(sentence).__name__)
print("Recursive:", type(recursive).__name__)