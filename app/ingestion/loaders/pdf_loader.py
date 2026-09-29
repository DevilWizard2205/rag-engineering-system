from pathlib import Path

from pypdf import PdfReader

from app.ingestion.document import Document


class PDFLoader:
    def load(self, file_path: str) -> list[Document]:
        path = Path(file_path)

        reader = PdfReader(path)

        documents = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            document = Document(
                id=f"{path.stem}_page_{page_number}",
                text=text,
                metadata={
                    "source": str(path),
                    "file_type": "pdf",
                    "file_name": path.name,
                    "page": page_number,
                },
            )

            documents.append(document)

        return documents