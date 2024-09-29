import requests
import allure

from data import Order, Response, Api


class TestCreateOrder:
    @allure.title('Получить заказы конкретного авторизованного пользователя')
    def test_receiving_orders_the_user_authorised(self, create_user_and_delete):
        _, create_response_json = create_user_and_delete  # Получаем пользователя и токен из фикстуры

        # Создание заказа
        requests.post(Api.BASE_URL + Api.ORDER_CREATE, data = Order.INGREDIENTS,
                                              headers = {'Authorization': create_response_json['accessToken']})

        # Запрос заказов авторизованного пользователя
        response = requests.get(Api.BASE_URL + Api.USER_ORDER, headers={'Authorization': create_response_json['accessToken']})
        response_json = response.json()

        assert response.status_code == 200, print(response.status_code)
        assert response_json.get('success') is True, print(response_json)
        assert 'total' in response_json != "", print(response_json)
        assert 'totalToday' in response_json != "", print(response_json)
        assert 'orders' in response_json, print(response_json)

    @allure.title('Получить заказы конкретного пользователя, не автризовавшегося в системе')
    def test_receiving_orders_without_authorised(self, create_user_and_delete):
        # Запрос заказов пользователя, не автризовавшегося в системе
        response = requests.get(Api.BASE_URL + Api.USER_ORDER)
        response_json = response.json()

        assert (response.status_code == 401 and response_json == Response.ERROR_YOU_SHOULD_BE_AUTHORISED), \
            f'Ожидался статус-код 401, но получили статус-код {response.status_code} и JSON {response_json}'
