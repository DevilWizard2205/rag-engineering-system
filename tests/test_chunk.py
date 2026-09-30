from app.ingestion.chunking.chunk import Chunk


chunk = Chunk(
    id="sample_0001",
    text="Retrieval Augmented Generation combines retrieval with generation.",
    metadata={
        "document_id": "sample",
        "source": "sample.txt",
        "chunk_index": 0,
    },
)


print("Chunk ID:", chunk.id)
print("Text:", chunk.text)
print("Metadata:", chunk.metadata)