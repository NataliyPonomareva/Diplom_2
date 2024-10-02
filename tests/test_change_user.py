import allure
import requests
import pytest

from data import User, Response, Api


class TestChangeUser:
    @allure.title('Изменение email пользователя с авторизацией')
    def test_change_email_authorized_user(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Отправляем PATCH-запрос для изменения email
        response = requests.patch(Api.BASE_URL + Api.USER_AUTH, headers={'Authorization': create_response_json['accessToken']}, json=User.USER_UPDATED_EMAIL)
        response_json = response.json()

        assert response.status_code == 200, print(response.status_code)
        assert response_json.get('success') is True, print(response_json)
        assert response_json['user']['email'] == User.USER_UPDATED_EMAIL['email'], print(response_json)
        assert response_json['user']['name'] == create_response_json['user']['name'], print(response_json)

    @allure.title('Изменение name пользователя с авторизацией')
    def test_change_name_authorized_user(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Отправляем PATCH-запрос для изменения email
        response = requests.patch(Api.BASE_URL + Api.USER_AUTH, headers={'Authorization': create_response_json['accessToken']}, json=User.USER_UPDATED_NAME)
        response_json = response.json()

        assert response.status_code == 200, print(response.status_code)
        assert response_json.get('success') is True, print(response_json)
        assert response_json['user']['email'] == create_response_json['user']['email'], print(response_json)
        assert response_json['user']['name'] == User.USER_UPDATED_NAME['name'], print(response_json)

    @allure.title('Изменение password пользователя с авторизацией')
    def test_change_password_authorized_user(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Отправляем PATCH-запрос для изменения email
        response = requests.patch(Api.BASE_URL + Api.USER_AUTH, headers={'Authorization': create_response_json['accessToken']}, json=User.USER_UPDATED_PASSWORD)
        response_json = response.json()

        assert response.status_code == 200, print(response.status_code)
        assert response_json.get('success') is True, print(response_json)
        assert response_json['user']['email'] == create_response_json['user']['email'], print(response_json)
        assert response_json['user']['name'] == create_response_json['user']['name'], print(response_json)

    @allure.title('Изменение email пользователя с авторизацией')
    @pytest.mark.parametrize('change_required_fields',
                             [User.USER_UPDATED_EMAIL, User.USER_UPDATED_PASSWORD, User.USER_UPDATED_NAME])
    def test_change_required_fields_without_authorized_user(self, create_user_and_delete, change_required_fields):
        # Отправляем PATCH-запрос для изменения email
        response = requests.patch(Api.BASE_URL + Api.USER_AUTH, json=change_required_fields)
        response_json = response.json()

        assert (response.status_code == 401 and response_json == Response.ERROR_YOU_SHOULD_BE_AUTHORISED), \
            f'Ожидался статус-код 401, но получили статус-код {response.status_code} и JSON {response_json}'
