import requests
import allure

from data import Order, Response
from tests.url_api import Api


class TestCreateOrder:
    @allure.title('Создание заказа с ингредиентами авторизованным пользователем')
    def test_create_order_with_ingredients_authorised(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Создание заказа
        response = requests.post(Api.BASE_URL + Api.ORDER_CREATE, data = Order.INGREDIENTS,
                                              headers = {'Authorization': create_response_json['accessToken']})
        response_json = response.json()

        assert (response.status_code == 200
                and response_json.get('success') is True
                and 'name' in response_json != ""
                and 'order' in response_json
                and 'number' in response_json['order'] != ""), \
                f'Ожидался статус-код 200, но получили статус-код {response.status_code} и JSON {response_json}'


    @allure.title('Создание заказа с ингредиентами пользователем, без указания токена авторизации')
    def test_create_order_with_ingredients_without_authorised(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Создание заказа
        response = requests.post(Api.BASE_URL + Api.ORDER_CREATE, data=Order.INGREDIENTS)
        response_json = response.json()

        assert (response.status_code == 200
                and response_json.get('success') is True
                and 'name' in response_json != ""
                and 'order' in response_json
                and 'number' in response_json['order'] != ""), \
            f'Ожидался статус-код 200, но получили статус-код {response.status_code} и JSON {response_json}'


    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_create_order_without_ingredients_authorised(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Создание заказа
        response = requests.post(Api.BASE_URL + Api.ORDER_CREATE, data = {},
                                              headers = {'Authorization': create_response_json['accessToken']})
        response_json = response.json()

        assert (response.status_code == 400 and response_json == Response.ERROR_INGREDIENT_IDS_MUST_BE_PROVIDED), \
            f'Ожидался статус-код 400, но получили статус-код {response.status_code} и JSON {response_json}'


    @allure.title('Создание заказа с неверным хешем ингредиентов авторизованным пользователем')
    def test_create_order_wrong_id_ingredients_authorised(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Создание заказа
        response = requests.post(Api.BASE_URL + Api.ORDER_CREATE, data = Order.INGREDIENTS_WRONG_ID,
                                              headers = {'Authorization': create_response_json['accessToken']})

        assert (response.status_code == 500, f'Ожидался статус-код 400, но получили статус-код {response.status_code}')
