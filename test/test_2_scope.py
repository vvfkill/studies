import pytest


@pytest.fixture(scope="class")
def computer():
    print("включаем комп")
    yield {
        "brand": "Apple",
        "ram": 16
    }
    print("выключаем комп")

class TestComputer:

    def test_brand(self, computer):
        assert computer["brand"] == "Apple"

    def test_ram(self, computer):
        assert computer["ram"] == 16
