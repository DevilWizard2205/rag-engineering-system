from pydantic import BaseModel, Field
from typing import Any


class Chunk(BaseModel):
    id: str
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)