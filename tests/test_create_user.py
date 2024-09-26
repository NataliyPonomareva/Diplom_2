import allure
import requests
import pytest

from data import User, Response
from tests.url_api import Api


class TestCreateUser:
    @allure.title('Можно создать уникального пользователя')
    def test_create_unique_user(self, create_user_and_delete):
        create_response, create_response_json = create_user_and_delete
        assert (create_response.status_code == 200
                 and create_response_json.get('success') is True
                 and 'accessToken' in create_response_json != ""
                 and 'refreshToken' in create_response_json != ""
                 and create_response_json['user']['email'] == User.USER_CREATE ['email']
                 and create_response_json['user']['name'] == User.USER_CREATE ['name']), \
                f'Ожидался статус-код 200, но получили статус-код {create_response_json.status_code} и JSON {create_response_json}'


    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_create_user_already_exists(self, create_user_and_delete):
        requests.post(Api.BASE_URL + Api.USER_CREATE, json=User.USER_CREATE)
        response = requests.post(Api.BASE_URL + Api.USER_CREATE, json=User.USER_CREATE)
        response_json = response.json()
        assert response.status_code == 403 and response_json == Response.USER_ALREADY_EXISTS, \
                f'Ожидался статус-код 403 и JSON {Response.USER_ALREADY_EXISTS}, но получили статус-код {response.status_code} и JSON {response_json}'

    @allure.title('Нельзя создать пользователя без указания email или пароля или имени')
    @pytest.mark.parametrize('user_without_required_fields', [User.USER_WITHOUT_EMAIL, User.USER_WITHOUT_PASSWORD, User.USER_WITHOUT_NAME])
    def test_create_user_without_required_fields(self, user_without_required_fields):
        response = requests.post(Api.BASE_URL + Api.USER_CREATE, json=user_without_required_fields)
        response_json = response.json()

        assert response.status_code == 403 and response_json == Response.ERROR_EMAIL_PASSWORD_NAME_ARE_REQUIRED_FIELDS, \
            f'Ожидался статус-код 403 и JSON {Response.ERROR_EMAIL_PASSWORD_NAME_ARE_REQUIRED_FIELDS}, но получили статус-код {response.status_code} и JSON {response_json}'
