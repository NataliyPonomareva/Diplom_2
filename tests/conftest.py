import allure
import pytest
import requests

from data import User
from tests.url_api import Api


@allure.title('Создание пользователя в начале теста, удаление тестовых данных пользователя - после завершения теста')
@pytest.fixture
def create_user_and_delete():
    # Создаем пользователя для теста
    create_response = requests.post(Api.BASE_URL + Api.USER_CREATE, json=User.USER_CREATE)
    create_response_json = create_response.json()

    yield create_response, create_response_json

    token = create_response_json['accessToken']
    requests.delete(Api.BASE_URL + Api.USER_DELETE, headers={'Authorization': token})
