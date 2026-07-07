import pytest
from deepeval import assert_test
from deepeval.test_case imprt LLMTestCase
from deepeval.metrics imort AnswerRelevanceMetric


def test_chatbot_is_relevant():
    test_case = LLMTestCase(
        input = "What are your hours?",
        actual_output = "We are open 9 to 5, Monday to Friday.",

    )
    metric = AnswerRelevancyMetric(threshold = 0.7)

    assert_test(test_case,[metric])

