from pathlib import Path

from app.ingestion.document import Document


def normalize_metadata(document: Document) -> Document:
    metadata = dict(document.metadata)

    source = metadata.get("source")

    if source:
        metadata["source"] = str(Path(source))

    metadata["file_name"] = metadata.get(
        "file_name",
        Path(source).name if source else None
    )

    metadata["file_type"] = metadata.get(
        "file_type",
        Path(source).suffix.lower().lstrip(".") if source else None
    )

    metadata["document_id"] = document.id

    metadata["content_hash"] = document.content_hash

    return document.copy(
        update={"metadata": metadata}
    )