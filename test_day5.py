import pytest
import json

@pytest.fixture
def goldens():
    with open("goldens.json") as f:
        return json.load(f)


def test_uses_fixture(goldens):              # ← goldens, not sample_golden
    for case in goldens:
        assert case["input"].endswith("?")


def test_expected_exists(goldens):           # ← goldens here too
    for case in goldens:
        assert "expected" in case, f"Missing 'expected' in: {case}"
        assert len(case["expected"]) > 0