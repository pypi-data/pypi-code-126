from src.models import ResponseModel


class SuitesApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_SUITES = "/suite/{}"
    _POST_CREATE_SUIT = "/suite/{}"
    _GET_SUIT_BY_ID = "/suite/{}/{}"
    _DELETE_SUIT = "/suite/{}/{}"
    _UPDATE_SUIT = "/suite/{}/{}"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-suites
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_SUITES.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-suite
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_SUIT.format(code)}",
            json=body,
        )

    def delete(self, code: str, uuid: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-suite
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}" f"{self._DELETE_SUIT.format(code, uuid)}",
        )

    def get_specific_suit(self, code: str, uuid: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-suite
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}" f"{self._GET_SUIT_BY_ID.format(code, uuid)}",
        )

    def update(self, code: str, uuid: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-suite
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}" f"{self._UPDATE_SUIT.format(code, uuid)}",
            json=body,
        )
