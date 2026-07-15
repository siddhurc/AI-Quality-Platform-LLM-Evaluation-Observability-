from sqlalchemy.orm import Session

from app.models.experiment_run import ExperimentRun


def create_experiment(
    db: Session,
    application_name: str,
    model_name: str,
    prompt_version: str
):

    experiment = ExperimentRun(

        application_name=application_name,

        model_name=model_name,

        prompt_version=prompt_version

    )

    db.add(experiment)

    db.commit()

    db.refresh(experiment)

    return experiment