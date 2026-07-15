from sqlalchemy.orm import Session

from app.models.metric import Metric


def save_metric(

    db: Session,

    evaluation_case_id: int,

    metric_name: str,

    score: float,

    threshold: float,

    passed: bool,

    reason: str

):

    metric = Metric(

        evaluation_case_id=evaluation_case_id,

        metric_name=metric_name,

        score=score,

        threshold=threshold,

        passed=passed,

        reason=reason

    )

    db.add(metric)

    db.commit()

    db.refresh(metric)

    return metric