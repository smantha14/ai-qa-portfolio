import json
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.models import AnthropicModel

# The judge model — same Claude setup that worked yesterday
judge = AnthropicModel(model="claude-sonnet-4-5", temperature=0)

# --- Fixture: load the golden dataset once (your Day 5 skill) ---
@pytest.fixture
def goldens():
    with open("goldens.json") as f:
        return json.load(f)

# --- Test 1: Answer Relevancy on the "relevancy" cases ---
def test_answer_relevancy(goldens):
    relevancy_cases = [g for g in goldens if g["category"] == "relevancy"]
    for case in relevancy_cases:
        test_case = LLMTestCase(
            input=case["input"],
            actual_output=case["expected_output"],   # for now we test the golden answer itself
        )
        metric = AnswerRelevancyMetric(threshold=0.7, model=judge)
        assert_test(test_case, [metric])

# --- Test 2: Faithfulness on the "faithfulness" cases ---
def test_faithfulness(goldens):
    faithfulness_cases = [g for g in goldens if g["category"] == "faithfulness"]
    for case in faithfulness_cases:
        test_case = LLMTestCase(
            input=case["input"],
            actual_output=case["expected_output"],
            retrieval_context=case["context"],       # faithfulness checks output against context
        )
        metric = FaithfulnessMetric(threshold=0.9, model=judge)
        assert_test(test_case, [metric])