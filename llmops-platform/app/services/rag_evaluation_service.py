from sqlalchemy.orm import Session

from app.models.evaluation_case import EvaluationCase

from app.services.rag_client import ask_rag

from app.services.evaluation_service import evaluate_evaluation_case


def evaluate_rag(
    db: Session,
    experiment_id: int,
    question: str,
    expected_output: str,
    department: str,
    metric_names: list[str]
):

    rag_result = ask_rag(
        question=question,
        department=department,
    )

    evaluation_case = EvaluationCase(

        experiment_id=experiment_id,

        input=question,

        expected_output=expected_output,

        actual_output=rag_result["answer"],

        context="\n".join(
            rag_result["retrieval_context"]
        ),

        retrieval_context="\n".join(
            rag_result["retrieval_context"]
        )

    )

    db.add(evaluation_case)

    db.commit()

    db.refresh(evaluation_case)

    metric_result = evaluate_evaluation_case(
    db=db,
    evaluation_case=evaluation_case,
    metric_names=metric_names
)

    return {

        "rag_response": rag_result,

        "evaluation": metric_result,

        "evaluation_case_id": evaluation_case.id

    }