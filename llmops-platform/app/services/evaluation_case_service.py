from sqlalchemy.orm import Session

from app.models.evaluation_case import EvaluationCase


def create_evaluation_case(
    db: Session,
    experiment_id: int,
    input: str,
    expected_output: str,
    actual_output: str | None,
    context: str | None,
    retrieval_context: str | None,
):

    evaluation_case = EvaluationCase(

        experiment_id=experiment_id,

        input=input,

        expected_output=expected_output,

        actual_output=actual_output,

        context=context,

        retrieval_context=retrieval_context

    )

    db.add(evaluation_case)

    db.commit()

    db.refresh(evaluation_case)

    return evaluation_case