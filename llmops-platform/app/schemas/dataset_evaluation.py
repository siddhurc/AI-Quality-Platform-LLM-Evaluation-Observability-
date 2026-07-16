from pydantic import BaseModel


class DatasetEvaluationRequest(BaseModel):

    experiment_id: int

    dataset_name: str

    metrics: list[str] = [
        "answer_relevancy",
        "faithfulness"
    ]