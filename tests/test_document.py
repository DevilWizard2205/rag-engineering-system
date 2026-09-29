from app.ingestion.document import Document


doc = Document(
    id="doc_001",
    text="Retrieval Augmented Generation combines retrieval with generation.",
    metadata={
        "source": "example.txt",
        "file_type": "txt",
        "page": 1
    }
)

print(doc)
print()
print("ID:", doc.id)
print("Text:", doc.text)
print("Source:", doc.metadata["source"])