from pathlib import Path
from app.ingestion.document import Document


class TXTLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        text = path.read_text(encoding="utf-8")

        return Document(
            id=path.stem,
            text=text,
            metadata={
                "source": str(path),
                "file_type": "txt",
                "file_name": path.name,
            },
        )