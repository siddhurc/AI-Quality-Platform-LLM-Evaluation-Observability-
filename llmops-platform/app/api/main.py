from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.experiment_run import ExperimentRun
from app.models.evaluation_case import EvaluationCase
from app.models.metric import Metric

from app.database.session import get_db

from app.schemas.experiment import (
    ExperimentCreate,
    ExperimentResponse
)

from app.services.evaluation_service import evaluate_evaluation_case
from app.services.experiment_service import (
    create_experiment
)

from app.schemas.evaluation_case import (
    EvaluationCaseCreate,
    EvaluationCaseResponse
)

from app.services.evaluation_case_service import (
    create_evaluation_case
)

from app.evaluators.deepeval_evaluator import evaluate_case

from app.services.metric_service import save_metric

from app.models.evaluation_case import EvaluationCase

from app.schemas.evaluate_rag import EvaluateRAGRequest
from app.services.rag_evaluation_service import evaluate_rag

from app.services.analytics_service import get_experiment_summary

from app.schemas.dataset_evaluation import DatasetEvaluationRequest
from app.services.dataset_evaluation_service import (
    evaluate_dataset as evaluate_dataset_service
)

from app.schemas.experiment_compare import ExperimentCompareRequest

from app.services.comparison_service import compare_experiments

app = FastAPI(
    title="Enterprise LLMOps Platform"
)


@app.post(
    "/experiments",
    response_model=ExperimentResponse
)
def create_new_experiment(

    experiment: ExperimentCreate,

    db: Session = Depends(get_db)

):

    return create_experiment(

        db,

        application_name=experiment.application_name,

        model_name=experiment.model_name,

        prompt_version=experiment.prompt_version

    )


@app.post(
    "/experiments/{experiment_id}/cases",
    response_model=EvaluationCaseResponse
)
def create_case(

    experiment_id: int,

    evaluation_case: EvaluationCaseCreate,

    db: Session = Depends(get_db)

):

    return create_evaluation_case(

        db=db,

        experiment_id=experiment_id,

        input=evaluation_case.input,

        expected_output=evaluation_case.expected_output,

        actual_output=evaluation_case.actual_output,

        context=evaluation_case.context,

        retrieval_context=evaluation_case.retrieval_context

    )



@app.post("/evaluation/{case_id}/evaluate")
def evaluate(

    case_id: int,

    db: Session = Depends(get_db)

):

    evaluation_case = db.get(
        EvaluationCase,
        case_id
    )

    if evaluation_case is None:

        return {
            "message": "Evaluation case not found."
        }

    return evaluate_evaluation_case(
    db=db,
    evaluation_case=evaluation_case
    )

    save_metric(

        db=db,

        evaluation_case_id=case_id,

        metric_name=result["metric_name"],

        score=result["score"],

        threshold=result["threshold"],

        passed=result["passed"]

    )

    return result


@app.post("/evaluate-rag")
def evaluate_rag_endpoint(
    request: EvaluateRAGRequest,
    db: Session = Depends(get_db)
):

    return evaluate_rag(
        db=db,
        experiment_id=request.experiment_id,
        question=request.question,
        expected_output=request.expected_output,
        department=request.department,
        metric_names=request.metrics
    )


@app.get("/experiments/{experiment_id}/summary")
def experiment_summary(
    experiment_id: int,
    db: Session = Depends(get_db)
):

    return get_experiment_summary(
        db=db,
        experiment_id=experiment_id
    )



@app.post("/evaluate-dataset")
def evaluate_dataset_endpoint(

    request: DatasetEvaluationRequest,

    db: Session = Depends(get_db)

):

    return evaluate_dataset_service(

        db=db,

        experiment_id=request.experiment_id,

        dataset_name=request.dataset_name,

        metric_names=request.metrics

    )


@app.post("/experiments/compare")
def compare(

    request: ExperimentCompareRequest,

    db: Session = Depends(get_db)

):

    return compare_experiments(

        db=db,

        experiment_ids=request.experiment_ids

    )