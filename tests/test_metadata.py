from app.ingestion.loader import DocumentLoader


loader = DocumentLoader()

documents = loader.load(
    "data/raw/sample.txt"
)

document = documents[0]

print("Document ID:", document.id)
print("Content hash:", document.content_hash)

print("Normalized metadata:")

for key, value in document.metadata.items():
    print(f"{key}: {value}")