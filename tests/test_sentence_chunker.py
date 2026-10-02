from app.ingestion.document import Document
from app.ingestion.chunking.sentence import SentenceChunker


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

chunker = SentenceChunker( 
    max_characters=120
)

chunks = chunker.chunk(document)

print("Number of chunks:", len(chunks))
print()

for chunk in chunks:
    print("ID:", chunk.id)
    print("Text:", chunk.text)
    print("Characters:", len(chunk.text))
    print("Metadata:", chunk.metadata)
    print("-" * 60)