from .config import DashConfig
from .Exceptions import MissingConfigData
from requests import post, get


class User:

    def __init__(self, secret_code: str):
        self.code: str = secret_code

    @staticmethod
    def _get_data(key: str) -> str:
        data = DashConfig[key]
        if not data:
            raise MissingConfigData
        return data

    @property
    def auth_token(self):
        data = {
            'client_id': self._get_data('CLIENT_ID'),
            'client_secret': self._get_data('CLIENT_SECRET'),
            'grant_type': 'authorization_code',
            'code': self.code,
            'redirect_uri': self._get_data('REDIRECT_URI')
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = post("https://discord.com/api/oauth2/token", data=data, headers=headers)
        response.raise_for_status()
        return response.json()['access_token']

    @staticmethod
    def data(auth_code: str):
        response = get(f"https://discord.com/api/oauth2/@me", headers={"Authorization": f"Bearer {auth_code}"})
        response.raise_for_status()
        return response.json()['user']

    @staticmethod
    def guilds(auth_code: str):
        response = get("https://discord.com/api/v8/users/@me/guilds", headers={"Authorization": f"Bearer {auth_code}"})
        response.raise_for_status()
        return response.json()
