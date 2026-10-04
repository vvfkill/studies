#@allure.title заголовок
#@allure.description описание
#@allure.feature
#@allure.story
#allure.step
import allure

@allure.feature("API")
@allure.story("GET api/anime")
@allure.title("Получение аниме по ID")
@allure.description(
    "Проверяет получение существующего аниме "
    "и корректность структуры ответа."
)
@allure.severity(allure.severity_level.NORMAL)
def test_get_anime_by_id(api_request):
    anime_id = 5

    with allure.step("Отправить GET-запрос"):
        response = api_request.get(
            f"http://127.0.0.1:8000/api/anime/{anime_id}"
        )

    with allure.step("Проверить статус ответа"):
        assert response.status == 200

    with allure.step("Проверить структуру ответа"):
        data = response.json()

        assert isinstance(data, dict)
        assert isinstance(data["animeId"], int)
        assert isinstance(data["titleOriginal"], str)
        assert isinstance(data["genres"], list)

    allure.attach(
        response.text(),
        name="Ответ API",
        attachment_type=allure.attachment_type.JSON
    )
