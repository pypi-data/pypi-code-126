from src.models import ResponseModel


class SearchApi:
    def __init__(self, app):
        self.app = app

    _GET_SEARCH = "/v1/search"

    def search(self, params: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/search-1
        """
        return self.app.client.request(
            method="GET", url=f"{self.app.base_path}{self._GET_SEARCH}", params=params
        )
