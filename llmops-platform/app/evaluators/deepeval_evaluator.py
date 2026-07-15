from dotenv import load_dotenv

from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

load_dotenv()


def evaluate_case(evaluation_case):

    metric = AnswerRelevancyMetric(
        model="gemini-2.5-flash",
        threshold=0.7
    )

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

    metric.measure(test_case)

    return {

        "metric_name": "Answer Relevancy",

        "score": metric.score,

        "passed": metric.success,

        "threshold": metric.threshold,

        "reason": metric.reason

    }