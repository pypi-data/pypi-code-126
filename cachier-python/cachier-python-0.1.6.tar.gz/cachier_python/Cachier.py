import requests


class Cachier:
    def __init__(self: 'Cachier', url: str) -> None:
        self.url = url

    def get(self: 'Cachier', key: str) -> object:
        if not key: return None

        url: str = f'{self.url}?cache_key={key}'
        response: requests.Response = requests.get(url)

        if response.status_code != 200: return None

        response_json: dict = response.json()

        if not response_json: return None

        return response_json['value']

    def set(self: 'Cachier', key: str, value: object, expiry: int | None = None) -> bool:
        if not key: return False

        url: str = f'{self.url}'
        response: requests.Response = requests.post(url, json={
            'cache_key': key,
            'cache_value': value,
            'cache_expiry': expiry
        })

        if response.status_code != 200: return False

        response_json: dict = response.json()

        if not response_json: return False

        return response_json['is_saved_successfully']
