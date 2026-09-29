from app.ingestion.loaders.pdf_loader import PDFLoader


loader = PDFLoader()

documents = loader.load("data/raw/sample.pdf")

print("Number of pages:", len(documents))
print()

for document in documents:
    print("ID:", document.id)
    print("Page:", document.metadata["page"])
    print("Source:", document.metadata["file_name"])
    print("Characters:", len(document.text))
    print("-" * 50)