#fixture с числом
# фикстура создаётся заново для каждого теста, который её использует
import pytest


@pytest.fixture
def number():
    return 10

def test_number(number):
    assert number == 10

#fixture со словарем
@pytest.fixture
def user():
    return {
        "name": "vika",
        "age": 10,
        "city": "ryazan"
    }

def test_user(user):
    assert isinstance(user,dict)
    assert user["name"] == "vika"
    assert user["age"] == 10
    assert user["city"] == "ryazan"

#fixture с функцией
@pytest.fixture
def calculator():
    def add(a,b):
        return a + b
    return add

def test_add(calculator):
    assert calculator(5,3) == 8
