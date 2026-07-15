from pydantic import BaseModel


class EvaluationCaseCreate(BaseModel):

    input: str

    expected_output: str

    actual_output: str | None = None

    context: str | None = None

    retrieval_context: str | None = None


class EvaluationCaseResponse(BaseModel):

    id: int

    experiment_id: int

    input: str

    expected_output: str

    actual_output: str | None

    context: str | None

    retrieval_context: str | None

    class Config:

        from_attributes = True