from app.ingestion.document import Document


class Deduplicator:

    def __init__(self):
        self.seen_hashes = set()

    def is_duplicate(self, document: Document) -> bool:
        if document.content_hash in self.seen_hashes:
            return True

        self.seen_hashes.add(document.content_hash)

        return False