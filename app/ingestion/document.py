from pydantic import BaseModel, Field
from typing import Any
from datetime import datetime, timezone

from pydantic import BaseModel, Field
from typing import Any
from datetime import datetime, timezone


from pydantic import BaseModel, Field
from typing import Any
from datetime import datetime, timezone

from app.ingestion.utils import generate_content_hash


class Document(BaseModel):
    id: str
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    content_hash: str = ""

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __init__(self, **data):
        if not data.get("content_hash"):
            data["content_hash"] = generate_content_hash(
                data.get("text", "")
            )

        super().__init__(**data)