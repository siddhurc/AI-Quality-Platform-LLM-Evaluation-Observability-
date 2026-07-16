import json
from pathlib import Path


DATASET_DIR = Path("dataset")


def load_dataset(dataset_name: str):

    dataset_path = DATASET_DIR / dataset_name

    if not dataset_path.exists():

        raise FileNotFoundError(
            f"{dataset_name} not found."
        )

    with open(dataset_path, "r", encoding="utf-8") as f:

        return json.load(f)