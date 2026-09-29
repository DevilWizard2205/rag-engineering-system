from app.ingestion.loaders.markdown_loader import MarkdownLoader


loader = MarkdownLoader()

document = loader.load("data/raw/sample.md")

print("Document ID:", document.id)
print()
print("Document text:")
print(document.text)
print()
print("Metadata:", document.metadata)