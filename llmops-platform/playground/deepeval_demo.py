from dotenv import load_dotenv

from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

load_dotenv()

metric = AnswerRelevancyMetric(
    model="gemini-2.5-flash",
    threshold=0.7
)

test_case = LLMTestCase(
    input="How many days of annual leave are employees entitled to?",

    actual_output="Employees are entitled to 20 days of annual leave.",

    expected_output="Employees are entitled to 20 days of annual leave."
)

metric.measure(test_case)

print("Score:", metric.score)
print("Passed:", metric.success)
print("Reason:")
print(metric.reason)