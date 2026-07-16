from sqlalchemy.orm import Session

from app.models.experiment_run import ExperimentRun


def get_all_experiments(db: Session):

    experiments = (

        db.query(ExperimentRun)

        .order_by(ExperimentRun.id.desc())

        .all()

    )

    return experiments