#scope определяет сколько раз pytest создает фикстуру и сколько она живет
#варианты scope:
#function - для каждого теста
#class - один раз на класс тестов
#module - один раз на файл
#session - один раз на весь запуск pytest

def test_name_user(user):
    assert user["name"] == "Vika"

def test_age_user(user):
    assert user["age"] == 21

def test_city_user(user):
    assert user["city"] == "Ryazan"

def test_work_user(user):
    assert user["work"] is True
