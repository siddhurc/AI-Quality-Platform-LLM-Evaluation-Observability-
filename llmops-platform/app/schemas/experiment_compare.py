from pydantic import BaseModel


class ExperimentCompareRequest(BaseModel):

    experiment_ids: list[int]