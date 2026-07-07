#functions
def is_relevant(score, threshold=0.7):
    return score >= threshold

def test_high_score_pass():
    result = is_relevant (0.9)
    assert result == True

def test_low_score_fail():
    result = is_relevant (0.5)
    assert result == False

test_high_score_pass()
test_low_score_fail()
print("All tests passed!")


def is_polite(response):
    return "please" in response or "thank" in response
assert is_polite("thank you for waiting") == True
assert is_polite("no") == False
print("Politeness tests passed!")

