from app.ingestion.loaders.html_loader import HTMLLoader


loader = HTMLLoader()

document = loader.load("data/raw/sample.html")

print("Document ID:", document.id)
print()
print("Document text:")
print(document.text)
print()
print("Metadata:", document.metadata)