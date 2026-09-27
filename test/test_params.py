import pytest


@pytest.mark.parametrize("number", [1, 5, 10, 20])
def test_number(number):
    assert number > 0

#################################################

@pytest.mark.parametrize(
    "name, age",
    [
        ("Vika", 21),
        ("Anton", 22),
        ("Kate", 19)
    ]
)
def test_user(name, age):
    assert isinstance(name, str)
    assert age >= 18
