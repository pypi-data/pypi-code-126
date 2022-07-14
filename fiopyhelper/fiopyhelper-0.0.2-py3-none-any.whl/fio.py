from fiopy.config import Config
from fiopy.enums import ConfigType
from fiopy.models.user import UserModel
from fiopy.http.http_request import HttpRequest

__all__ = ["Fio"]


class Fio:
    @staticmethod
    def login(*, email: str = None, password: str = None, token: str = None, **kwargs):
        user_data = {}
        user_data.update(kwargs)
        print("AM I HEREREERE")
        if email and password:
            response = (
                HttpRequest(Config.api["v2"]["hostname"])
                .post(Config.api["v2"]["endpoints"]["login"])
                .body({"email": email, "password": password})
                .send()
            )
            print(response.body)
            if response.status().is_equal_to(200):
                session_jwt = response.header("authorization").get()
                user_data.update(response.body().get())
                user_data.update({"session_jwt": session_jwt})
        else:
            session_pat = token
            user_data.update({"session_pat": session_pat})
        print("logging with FIO")
        model = UserModel(**user_data)
        Fio._set_default_user(model)
        return model

    @staticmethod
    def _set_default_user(user: UserModel = None):
        Config.update_config(config=user, config_type=ConfigType.USER)

    @staticmethod
    def update_config(config, config_type):
        Config.update_config(config=config, config_type=config_type)

    @staticmethod
    def default_user():
        return Config.user
