from pydantic import BaseModel, Field


class EvaluationQuestion(BaseModel):
    id: str
    question: str
    category: str
    expected_answer: str | None = None
    expected_sources: list[str] = Field(default_factory=list)
    should_abstain: bool = False