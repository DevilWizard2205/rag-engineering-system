from pathlib import Path

from bs4 import BeautifulSoup

from app.ingestion.document import Document


class HTMLLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        html = path.read_text(encoding="utf-8")

        soup = BeautifulSoup(html, "html.parser")

        for element in soup(["script", "style"]):
            element.decompose()

        text = soup.get_text(separator="\n", strip=True)

        title = soup.title.string.strip() if soup.title and soup.title.string else None

        return Document(
            id=path.stem,
            text=text,
            metadata={
                "source": str(path),
                "file_type": "html",
                "file_name": path.name,
                "title": title,
            },
        )