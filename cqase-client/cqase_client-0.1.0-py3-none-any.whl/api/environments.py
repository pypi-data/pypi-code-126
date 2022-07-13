from src.models import ResponseModel


class EnvironmentsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_ENV = "/environment/{}"
    _POST_CREATE_ENV = "/environment/{}"
    _GET_SPECIFIC_ENV = "/environment/{}/{}"
    _DELETE_ENV = "/environment/{}/{}"
    _UPDATE_ENV = "/environment/{}/{}"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-environments
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_ENV.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-environment
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_ENV.format(code)}",
            json=body,
        )

    def get_specific_env(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-environment
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_SPECIFIC_ENV.format(code, uuid)}",
        )

    def delete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-environment
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_ENV.format(code, uuid)}",
        )

    def update(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-environment
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_ENV.format(code, uuid)}",
            json=body,
        )
