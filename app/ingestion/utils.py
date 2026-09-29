import hashlib


def generate_content_hash(text: str) -> str:
    """
    Generate a stable SHA-256 hash for document content.
    """

    normalized_text = text.strip()

    return hashlib.sha256(
        normalized_text.encode("utf-8")
    ).hexdigest()