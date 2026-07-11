"""Fast structural checks — no API calls. These run in CI on every push."""
import json
import os

def load_goldens():
    path = os.path.join(os.path.dirname(__file__), "goldens.json")
    with open(path) as f:
        return json.load(f)

def test_goldens_file_is_valid_json():
    data = load_goldens()
    assert isinstance(data, list)
    assert len(data) > 0

def test_every_case_has_required_fields():
    for case in load_goldens():
        assert "id" in case, f"Missing id in {case}"
        assert "category" in case, f"Missing category in {case}"
        assert "input" in case and case["input"], f"Missing/empty input in {case['id']}"
        assert "expected_output" in case, f"Missing expected_output in {case['id']}"

def test_case_ids_are_unique():
    ids = [c["id"] for c in load_goldens()]
    assert len(ids) == len(set(ids)), "Duplicate case IDs found"

def test_all_categories_are_known():
    known = {"relevancy", "faithfulness", "bias", "toxicity", "pii", "injection", "overrefusal", "disclaimer"}
    for case in load_goldens():
        assert case["category"] in known, f"Unknown category: {case['category']} in {case['id']}"

def test_dataset_covers_core_risks():
    cats = {c["category"] for c in load_goldens()}
    for required in ["relevancy", "faithfulness", "pii", "bias"]:
        assert required in cats, f"Dataset missing coverage for: {required}"