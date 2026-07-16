import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API_URL = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="Enterprise LLMOps Platform",
    page_icon="🚀",
    layout="wide"
)



# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🚀 Enterprise LLMOps")

st.sidebar.markdown("---")

# -----------------------------
# Main Title
# -----------------------------

st.title("📊 Enterprise LLMOps Platform")

st.caption("LLM Evaluation • DeepEval • Enterprise RAG")

st.markdown("---")

# -----------------------------
# Load Experiments
# -----------------------------

try:

    response = requests.get(f"{API_URL}/experiments")

    response.raise_for_status()

    experiments = response.json()

except Exception as e:

    st.error(f"Unable to connect to backend.\n\n{e}")

    st.stop()

if len(experiments) == 0:

    st.warning("No experiments found.")

    st.stop()

# -----------------------------
# Experiment Selector
# -----------------------------

experiment_lookup = {

    f"Experiment {exp['id']} | {exp['prompt_version']} | {exp['model_name']}": exp

    for exp in experiments

}

selected = st.sidebar.selectbox(

    "Select Experiment",

    list(experiment_lookup.keys())

)

experiment = experiment_lookup[selected]

# -----------------------------
# Sidebar Experiment Info
# -----------------------------

st.sidebar.markdown("---")

st.sidebar.subheader("Experiment Details")

st.sidebar.write(f"**ID:** {experiment['id']}")

st.sidebar.write(f"**Application:** {experiment['application_name']}")

st.sidebar.write(f"**Model:** {experiment['model_name']}")

st.sidebar.write(f"**Prompt Version:** {experiment['prompt_version']}")

# -----------------------------
# Load Summary
# -----------------------------

summary = requests.get(

    f"{API_URL}/experiments/{experiment['id']}/summary"

).json()

df = pd.DataFrame(summary)

# -----------------------------
# Clean Metric Names
# -----------------------------

df["metric_name"] = df["metric_name"].replace({

    "AnswerRelevancyMetric": "Answer Relevancy",

    "FaithfulnessMetric": "Faithfulness",

    "ContextualPrecisionMetric": "Context Precision",

    "ContextualRelevancyMetric": "Context Relevancy"

})

# -----------------------------
# Round Values
# -----------------------------

df["average_score"] = df["average_score"].round(2)

df = df.sort_values("metric_name")

# -----------------------------
# Experiment Cards
# -----------------------------

st.subheader("Experiment Overview")

col1, col2, col3 = st.columns(3)

col1.metric(

    "Experiment ID",

    experiment["id"]

)

col2.metric(

    "Model",

    experiment["model_name"]

)

col3.metric(

    "Prompt Version",

    experiment["prompt_version"]

)

st.markdown("---")

# -----------------------------
# Summary Table
# -----------------------------

st.subheader("Evaluation Summary")

st.dataframe(

    df,

    hide_index=True,

    use_container_width=True

)

st.markdown("---")

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns(2)

with left:

    st.subheader("Average Metric Scores")

    fig = px.bar(

        df,

        x="metric_name",

        y="average_score",

        text="average_score",

        title="Average Scores"

    )

    fig.update_traces(textposition="outside")

    fig.update_layout(

        yaxis_range=[0, 1.1]

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

with right:

    st.subheader("Pass Rate")

    fig2 = px.bar(

        df,

        x="metric_name",

        y="pass_rate",

        text="pass_rate",

        title="Pass Rate (%)"

    )

    fig2.update_traces(textposition="outside")

    fig2.update_layout(

        yaxis_range=[0, 100]

    )

    st.plotly_chart(

        fig2,

        use_container_width=True

    )

st.markdown("---")

# -----------------------------
# Metric Progress
# -----------------------------

st.subheader("Metric Health")

for _, row in df.iterrows():

    st.write(f"### {row['metric_name']}")

    st.progress(float(row["average_score"]))

    c1, c2 = st.columns(2)

    c1.metric(

        "Average Score",

        row["average_score"]

    )

    c2.metric(

        "Pass Rate",

        f"{row['pass_rate']}%"

    )

    st.divider()