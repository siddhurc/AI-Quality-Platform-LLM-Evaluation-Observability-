from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from app.database.base import Base


class ExperimentRun(Base):

    __tablename__ = "experiment_runs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    application_name = Column(
        String(100),
        nullable=False
    )

    model_name = Column(
        String(100),
        nullable=False
    )

    prompt_version = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    evaluation_cases = relationship(
    "EvaluationCase",
    back_populates="experiment",
    cascade="all, delete-orphan"
)