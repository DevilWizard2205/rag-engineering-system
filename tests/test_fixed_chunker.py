from app.ingestion.document import Document
from app.ingestion.chunking.fixed import FixedSizeChunker


document = Document(
    id="doc_001",
    text=(
        "Retrieval Augmented Generation combines retrieval "
        "with generation. "
        "The retriever finds relevant information from a "
        "knowledge base. "
        "The language model then uses that information "
        "to generate an answer."
    ),
    metadata={
        "source": "example.txt",
        "file_type": "txt",
    },
)


chunker = FixedSizeChunker(
    chunk_size=100,
    overlap=20,
)

chunks = chunker.chunk(document)


print("Number of chunks:", len(chunks))
print()

for chunk in chunks:
    print("ID:", chunk.id)
    print("Text:", chunk.text)
    print("Metadata:", chunk.metadata)
    print("-" * 60)