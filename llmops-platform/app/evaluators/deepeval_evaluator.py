import os

from dotenv import load_dotenv

from deepeval.test_case import LLMTestCase

from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRelevancyMetric,
)

load_dotenv()

# Read model name from .env
MODEL_NAME = os.getenv("GOOGLE_MODEL", "gemini-3.1-flash-lite")


def evaluate_case(evaluation_case):

    metrics = [

        AnswerRelevancyMetric(
            threshold=0.7,
            model=MODEL_NAME
        ),

        FaithfulnessMetric(
            threshold=0.7,
            model=MODEL_NAME
        ),

        ContextualPrecisionMetric(
            threshold=0.7,
            model=MODEL_NAME
        ),

        ContextualRelevancyMetric(
            threshold=0.7,
            model=MODEL_NAME
        )

    ]

    test_case = LLMTestCase(

        input=evaluation_case.input,

        actual_output=evaluation_case.actual_output,

        expected_output=evaluation_case.expected_output,

        retrieval_context=(
            [evaluation_case.retrieval_context]
            if evaluation_case.retrieval_context
            else []
        ),

        context=(
            [evaluation_case.context]
            if evaluation_case.context
            else []
        )

    )

    results = []

    for metric in metrics:

        metric.measure(test_case)

        results.append({

            "metric_name": metric.__class__.__name__,

            "score": metric.score,

            "passed": metric.success,

            "threshold": metric.threshold,

            "reason": metric.reason

        })

    return results