import pytest
from morse import decode

@pytest.mark.parametrize("test_input,expected", [
    (".-", "A"),
    ("...", "S"),
    ("... --- ...", "SOS"),
    ('', ''),])

def test_decode(test_input, expected):
    assert decode(test_input) == expected
