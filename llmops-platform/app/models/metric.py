from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from app.database.base import Base


class Metric(Base):

    __tablename__ = "metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    evaluation_case_id = Column(
        Integer,
        ForeignKey("evaluation_cases.id"),
        nullable=False
    )

    metric_name = Column(
        String(100),
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    threshold = Column(
        Float,
        nullable=True
    )

    passed = Column(
        Boolean,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    evaluation_case = relationship(
        "EvaluationCase",
        back_populates="metrics"
    )

    reason = Column(
    Text,
    nullable=True
)