from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class EvaluationCase(Base):

    __tablename__ = "evaluation_cases"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    experiment_id = Column(
        Integer,
        ForeignKey("experiment_runs.id"),
        nullable=False
    )

    # DeepEval LLMTestCase fields

    input = Column(
        Text,
        nullable=False
    )

    expected_output = Column(
        Text,
        nullable=False
    )

    actual_output = Column(
        Text,
        nullable=True
    )

    context = Column(
        Text,
        nullable=True
    )

    retrieval_context = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    experiment = relationship(
        "ExperimentRun",
        back_populates="evaluation_cases"
    )

    metrics = relationship(
    "Metric",
    back_populates="evaluation_case",
    cascade="all, delete-orphan"
)