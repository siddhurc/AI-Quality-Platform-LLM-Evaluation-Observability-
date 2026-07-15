from app.database.base import Base
from app.database.session import engine

from app.models.experiment_run import ExperimentRun
from app.models.evaluation_case import EvaluationCase
from app.models.metric import Metric

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")