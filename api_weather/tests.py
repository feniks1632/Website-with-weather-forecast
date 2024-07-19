import requests
from api_weather.views import request_to_api

# Создаем фиктивный запрос
class FakeRequest:
    def __init__(self):
        self.user_id = "test_user"
        self.city = "Оренбург"
        self.search_time = "2024-07-19 17:47:00"


# Тестируем функцию
def test_request_to_api():
    request = FakeRequest()
    response = request_to_api(request)
    print(response)

test_request_to_api()