from app.ingestion.document import Document
from app.ingestion.deduplication import Deduplicator


deduplicator = Deduplicator()


document_1 = Document(
    id="doc_1",
    text="This is the same content.",
)

document_2 = Document(
    id="doc_2",
    text="This is the same content.",
)

document_3 = Document(
    id="doc_3",
    text="This is different content.",
)


print("Document 1 duplicate:", deduplicator.is_duplicate(document_1))
print("Document 2 duplicate:", deduplicator.is_duplicate(document_2))
print("Document 3 duplicate:", deduplicator.is_duplicate(document_3))