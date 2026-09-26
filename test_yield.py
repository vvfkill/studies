#yield позволяет fixture сделать что-то до теста,
#передать результат тесту, а потом сделать что-то после теста.
import pytest


@pytest.fixture
def tovar():  #подгототавливаем данные и отправляем их тесту
    yield {
        "name": "Laptop"
    }
def test_tovar(tovar): #тест
    assert tovar["name"] == "Laptop"

#1 задание - компьютер
@pytest.fixture

def computer():
    print("включаем компьютер")
    yield {
        "brand": "Apple",
        "ram": 16
    }
    print("отключаем компьютер")

def test_computer(computer):
    assert computer["brand"] == "Apple"
    assert computer["ram"] == 16

#2 задание - бронирование
@pytest.fixture
def booking():
    print("создаем бронирование")
    yield {
        "hotel":"Hitton",
        "nights": 3
    }
    print("отменяем бронирование")

def test_booking(booking):
    assert booking["hotel"] == "Hitton"
    assert booking["nights"] == 3
