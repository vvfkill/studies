import pytest


@pytest.fixture()
def user():
    yield {
        "name": "Vika",
        "age": 20,
        "is_active": True
    }
@pytest.fixture()
def product():
    yield {
        "name": "MacBook",
        "price": 1500,
        "in_stock": True
    }
@pytest.fixture()
def order(user, product):
    print("создаем заказ")

    yield {
        "user": user,
        "product": product,
        "quantity": 2
    }

    print("удаляем заказ")
