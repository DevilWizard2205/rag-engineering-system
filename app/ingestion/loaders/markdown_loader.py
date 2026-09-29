from pathlib import Path

from markdown import markdown

from app.ingestion.document import Document


class MarkdownLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        markdown_text = path.read_text(encoding="utf-8")

        html = markdown(markdown_text)

        text = html.replace("<p>", "").replace("</p>", "\n")
        text = text.replace("<h1>", "").replace("</h1>", "\n")
        text = text.replace("<h2>", "").replace("</h2>", "\n")
        text = text.replace("<h3>", "").replace("</h3>", "\n")

        return Document(
            id=path.stem,
            text=text.strip(),
            metadata={
                "source": str(path),
                "file_type": "markdown",
                "file_name": path.name,
            },
        )