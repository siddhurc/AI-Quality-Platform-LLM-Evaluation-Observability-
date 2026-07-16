from datetime import datetime

from pydantic import BaseModel


class ExperimentCreate(BaseModel):

    application_name: str

    model_name: str

    prompt_version: str


class ExperimentResponse(BaseModel):

    id: int

    application_name: str

    model_name: str

    prompt_version: str

    created_at: datetime

    class Config:

        from_attributes = True