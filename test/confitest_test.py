def test_user(user):
    assert user["age"] == 20
    assert user["is_active"] is True

def test_product(product):
    assert product["price"] == 1500
    assert product["in_stock"] is True

def test_order(order):
    assert order["quantity"] == 2

    assert order["user"]["name"] == "Vika"
    assert order["user"]["is_active"] is True

    assert order["product"]["name"] == "MacBook"
    assert order["product"]["in_stock"] is True
