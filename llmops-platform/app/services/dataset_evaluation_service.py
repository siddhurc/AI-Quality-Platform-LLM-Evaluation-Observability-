from app.services.dataset_loader import load_dataset
from app.services.rag_evaluation_service import evaluate_rag
from app.services.analytics_service import get_experiment_summary


def evaluate_dataset(
    db,
    experiment_id: int,
    dataset_name: str,
    metric_names: list[str]
):

    dataset = load_dataset(dataset_name)

    results = []

    for index, case in enumerate(dataset, start=1):

        print(f"\nEvaluating {index}/{len(dataset)}")
        print(f"Question: {case['question']}")

        result = evaluate_rag(

            db=db,

            experiment_id=experiment_id,

            question=case["question"],

            expected_output=case["expected_output"],

            department=case["department"],

            metric_names=metric_names

        )

        results.append(result)

    summary = get_experiment_summary(

        db=db,

        experiment_id=experiment_id

    )

    return {

        "experiment_id": experiment_id,

        "dataset_name": dataset_name,

        "total_cases": len(dataset),

        "summary": summary

    }