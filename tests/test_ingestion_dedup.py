from app.ingestion.loader import DocumentLoader
from app.ingestion.deduplication import Deduplicator


loader = DocumentLoader()
deduplicator = Deduplicator()


files = [
    "data/raw/sample.txt",
    "data/raw/sample.txt",
    "data/raw/sample.md",
    "data/raw/sample.md",
    "data/raw/sample.pdf",
]


for file_path in files:

    print("=" * 60)
    print("File:", file_path)

    documents = loader.load(file_path)

    if not isinstance(documents, list):
        documents = [documents]

    for document in documents:

        duplicate = deduplicator.is_duplicate(document)

        print(
            "ID:",
            document.id,
            "| Duplicate:",
            duplicate
        )