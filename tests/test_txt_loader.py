from app.ingestion.loaders.txt_loader import TXTLoader


loader = TXTLoader()

document = loader.load("data/raw/sample.txt")

print("Document ID:", document.id)
print("Document text:")
print(document.text)
print()
print("Metadata:", document.metadata)