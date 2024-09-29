class Api:
    BASE_URL = 'https://stellarburgers.nomoreparties.site' # Сервис  Stellar Burgers
    USER_CREATE = '/api/auth/register' # Создание пользователя
    USER_LOGIN = '/api/auth/login' # Логин пользователя
    USER_AUTH = '/api/auth/user' # Изменение данных пользователя
    ORDER_CREATE ='/api/orders' # Создание заказа
    USER_ORDER = '/api/orders' # Получение заказов конкретного пользователя
    USER_DELETE = '/api/auth/user' # Удаление пользователя

class User:
    USER_CREATE = {
                    "email": "user-create@gmail.com",
                    "password": "user333",
                    "name": "UserIvan1"
                    }

    USER_AUTHORIZATION = {
                    "email": "user-create@gmail.com",
                    "password": "user333"
                    }

    USER_WITHOUT_EMAIL = {
                    "password": "user333",
                    "name": "UserIvan1"
                    }

    USER_WITHOUT_PASSWORD = {
                    "email": "user-create@gmail.com",
                    "name": "UserIvan1"
                    }

    USER_WITHOUT_NAME = {
                    "email": "user-create@gmail.com",
                    "password": "user333"
                    }

    USER_WRONG_LOGIN = {
                    "email": "user_WRONG@gmail.com",
                    "password": "user333"
                    }

    USER_WRONG_PASSWORD = {
                    "email": "user-create@gmail.com",
                    "password": "WRONG"
                    }

    USER_UPDATED_EMAIL = {
                    "email": "user_updated_email@ya.ru"
                    }

    USER_UPDATED_NAME = {
                    "name": "UPDATED_NAME"
                    }

    USER_UPDATED_PASSWORD = {
                    "password": "user_updated_password"
                    }



class Response:
    USER_ALREADY_EXISTS = {
                    "success": False,
                    "message": "User already exists"
                    }

    ERROR_EMAIL_PASSWORD_NAME_ARE_REQUIRED_FIELDS = {
                    "success": False,
                    "message": "Email, password and name are required fields"
                    }

    ERROR_EMAIL_OR_PASSWORD_ARE_INCORRECT = {
                    "success": False,
                    "message": "email or password are incorrect"
                    }

    ERROR_YOU_SHOULD_BE_AUTHORISED = {
                    "success": False,
                    "message": "You should be authorised"
                    }

    ERROR_INGREDIENT_IDS_MUST_BE_PROVIDED = {
                    "success": False,
                    "message": "Ingredient ids must be provided"
                    }


class Order:
    INGREDIENTS = {
                    'ingredients': ['61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6d']
                    }

    INGREDIENTS_WRONG_ID = {
                    'ingredients': ['wrong_id', '61c0c5a71d1f82001bdaaa6d']
                    }