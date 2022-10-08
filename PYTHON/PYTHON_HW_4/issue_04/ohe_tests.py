import pytest
from one_hot_encoder import fit_transform

@pytest.mark.parametrize("test_input,expected", [
    (['Moscow', 'New York', 'Moscow', 'London'], [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]),
    (['Moscow'], [('Moscow', [1])]),
    (['Moscow', 'Moscow'], [ ('Moscow', [1]), ('Moscow', [1])]),])

def test_fit_transform(test_input, expected):
    assert fit_transform(test_input) == expected


def test_try_encode_wrong_type():
    with pytest.raises(TypeError):
        fit_transform(1)