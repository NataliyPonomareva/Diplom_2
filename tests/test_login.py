import allure
import requests
import pytest

from data import User, Response
from tests.url_api import Api


class TestAuthorizationUser:
    @allure.title('Авторизация под существующим пользователем')
    def test_authorization_user_exists(self, create_user_and_delete):
        response = requests.post(Api.BASE_URL + Api.USER_LOGIN, json=User.USER_CREATE)
        response_json = response.json()

        assert (response.status_code == 200
                and response_json.get('success') is True
                and 'accessToken' in response_json != ""
                and 'refreshToken' in response_json != ""
                and response_json['user']['email'] == User.USER_CREATE ['email']
                and response_json['user']['name'] == User.USER_CREATE ['name']), \
                f'Ожидался статус-код 200, но получили статус-код {response.status_code} и JSON {response_json}'


    @allure.title('Авторизация с неверным логином или паролем')
    @pytest.mark.parametrize('authorization_wrong_required_fields',
                             [User.USER_WRONG_LOGIN, User.USER_WRONG_PASSWORD])
    def test_authorization_wrong_required_fields(self, create_user_and_delete, authorization_wrong_required_fields):
        response = requests.post(Api.BASE_URL + Api.USER_LOGIN, json=authorization_wrong_required_fields)
        response_json = response.json()

        assert (response.status_code == 401 and response_json == Response.ERROR_EMAIL_OR_PASSWORD_ARE_INCORRECT), \
                f'Ожидался статус-код 401 и JSON {Response.ERROR_EMAIL_OR_PASSWORD_ARE_INCORRECT}, но получили статус-код {response.status_code} и JSON {response_json}'
