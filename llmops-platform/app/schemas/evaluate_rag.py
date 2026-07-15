from pydantic import BaseModel


class EvaluateRAGRequest(BaseModel):

    experiment_id: int

    question: str

    expected_output: str

    department: str