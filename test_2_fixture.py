#{
    #"name": "Laptop",
    #"price": 1000,
    #"in_stock": True
#}
import pytest


@pytest.fixture

def magazin():
    return {
        "name": "Laptop",
        "price": 1000,
        "in_stock": True
    }

def test_name(magazin):
    assert magazin["name"] == "Laptop"

def test_price(magazin):
    assert magazin["price"] == 1000

def test_in_stock(magazin):
    assert magazin["in_stock"] is True #можно использовать, как is, так и ==
