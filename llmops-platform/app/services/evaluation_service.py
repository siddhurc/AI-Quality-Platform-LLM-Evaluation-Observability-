from sqlalchemy.orm import Session

from app.models.evaluation_case import EvaluationCase

from app.evaluators.deepeval_evaluator import evaluate_case

from app.services.metric_service import save_metric


def evaluate_evaluation_case(
    db: Session,
    evaluation_case: EvaluationCase,
    metric_names: list[str]
):

    results = evaluate_case(
    evaluation_case,
    metric_names
)

    for result in results:

        save_metric(
            db=db,
            evaluation_case_id=evaluation_case.id,
            metric_name=result["metric_name"],
            score=result["score"],
            threshold=result["threshold"],
            passed=result["passed"],
            reason=result["reason"]
        )

    return results