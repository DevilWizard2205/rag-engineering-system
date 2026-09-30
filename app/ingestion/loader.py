from pathlib import Path

from app.ingestion.loaders.txt_loader import TXTLoader
from app.ingestion.loaders.pdf_loader import PDFLoader
from app.ingestion.loaders.markdown_loader import MarkdownLoader
from app.ingestion.loaders.html_loader import HTMLLoader
from app.ingestion.metadata import normalize_metadata

class DocumentLoader:

    def __init__(self):
        self.loaders = {
            ".txt": TXTLoader(),
            ".pdf": PDFLoader(),
            ".md": MarkdownLoader(),
            ".html": HTMLLoader(),
        }

    def load(self, file_path: str):

        path = Path(file_path)

        extension = path.suffix.lower()

        if extension not in self.loaders:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        loader = self.loaders[extension]

        documents = loader.load(file_path)

        if not isinstance(documents, list):
            documents = [documents]

        documents = [
            normalize_metadata(document)
            for document in documents
        ]

        return documents