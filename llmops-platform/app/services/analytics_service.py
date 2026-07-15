from sqlalchemy.orm import Session
from sqlalchemy import func, case

from app.models.metric import Metric
from app.models.evaluation_case import EvaluationCase


def get_experiment_summary(
    db: Session,
    experiment_id: int
):

    rows = (
        db.query(

            Metric.metric_name,

            func.avg(Metric.score).label("avg_score"),

            func.count(Metric.id).label("total_cases"),

            func.sum(
                case(
                    (Metric.passed == True, 1),
                    else_=0
                )
            ).label("passed_cases")

        )

        .join(
            EvaluationCase,
            Metric.evaluation_case_id == EvaluationCase.id
        )

        .filter(
            EvaluationCase.experiment_id == experiment_id
        )

        .group_by(
            Metric.metric_name
        )

        .all()
    )

    summary = []

    for metric_name, avg_score, total_cases, passed_cases in rows:

        passed_cases = passed_cases or 0

        summary.append({

            "metric_name": metric_name,

            "average_score": round(float(avg_score), 3),

            "total_cases": total_cases,

            "passed": passed_cases,

            "failed": total_cases - passed_cases,

            "pass_rate": round(
                (passed_cases / total_cases) * 100,
                2
            )

        })

    return summary