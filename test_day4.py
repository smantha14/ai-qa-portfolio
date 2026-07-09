def is_polite(response):
    return "please" in response or "thank" in response

def test_polite_respose_passes():
    assert is_polite ("thank you for waiting") == True

def test_polite_response_fails():
    assert is_polite ("no.") == False

def test_please_counts_as_polite():
    assert is_polite ("please hold") == True

def test_this_will_fail():
    assert is_polite ("go away") ==  False
