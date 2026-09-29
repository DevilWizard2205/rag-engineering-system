from app.ingestion.loader import DocumentLoader


loader = DocumentLoader()

files = [
    "data/raw/sample.txt",
    "data/raw/sample.pdf",
    "data/raw/sample.md",
    "data/raw/sample.html",
]

for file_path in files:

    print("=" * 60)
    print("Testing:", file_path)

    documents = loader.load(file_path)

    if not isinstance(documents, list):
        documents = [documents]

    print("Documents returned:", len(documents))

    for document in documents[:2]:
        print("ID:", document.id)
        print("Type:", document.metadata["file_type"])
        print("Characters:", len(document.text))