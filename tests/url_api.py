class Api:
    BASE_URL = 'https://stellarburgers.nomoreparties.site' # Сервис  Stellar Burgers
    USER_CREATE = '/api/auth/register' # Создание пользователя
    USER_LOGIN = '/api/auth/login' # Логин пользователя
    USER_AUTH = '/api/auth/user' # Изменение данных пользователя
    ORDER_CREATE ='/api/orders' # Создание заказа
    USER_ORDER = '/api/orders' # Получение заказов конкретного пользователя
    USER_DELETE = '/api/auth/user' # Удаление пользователя