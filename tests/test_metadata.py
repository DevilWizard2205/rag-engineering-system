from app.ingestion.loader import DocumentLoader
from app.ingestion.metadata import normalize_metadata


loader = DocumentLoader()

document = loader.load("data/raw/sample.txt")

document = normalize_metadata(document)

print("Document ID:", document.id)
print("Content hash:", document.content_hash)
print()
print("Normalized metadata:")

for key, value in document.metadata.items():
    print(f"{key}: {value}")