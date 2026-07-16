import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8001"

st.title("📈 Compare Experiments")

experiments = requests.get(
    f"{API_URL}/experiments"
).json()

lookup = {
    f"Experiment {e['id']} ({e['prompt_version']})": e["id"]
    for e in experiments
}

selected = st.multiselect(
    "Select Experiments",
    list(lookup.keys())
)

if len(selected) >= 2:

    ids = [
        lookup[s]
        for s in selected
    ]

    comparison = requests.post(

        f"{API_URL}/experiments/compare",

        json={
            "experiment_ids": ids
        }

    ).json()

    rows = []

    for experiment in comparison:

        for metric, values in experiment["metrics"].items():

            rows.append({

                "Experiment": experiment["experiment_id"],

                "Prompt": experiment["prompt_version"],

                "Metric": metric,

                "Average Score": values["average_score"],

                "Pass Rate": values["pass_rate"]

            })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("Select at least two experiments.")