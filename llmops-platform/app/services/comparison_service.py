from sqlalchemy.orm import Session

from app.models.experiment_run import ExperimentRun

from app.services.analytics_service import get_experiment_summary


def compare_experiments(

    db: Session,

    experiment_ids: list[int]

):

    comparison = []

    for experiment_id in experiment_ids:

        experiment = db.get(
            ExperimentRun,
            experiment_id
        )

        if experiment is None:
            continue

        summary = get_experiment_summary(
            db=db,
            experiment_id=experiment_id
        )

        metrics = {}

        for metric in summary:

            metrics[metric["metric_name"]] = {

                "average_score": metric["average_score"],

                "pass_rate": metric["pass_rate"]

            }

        comparison.append({

            "experiment_id": experiment.id,

            "application_name": experiment.application_name,

            "model_name": experiment.model_name,

            "prompt_version": experiment.prompt_version,

            "metrics": metrics

        })

    return comparison