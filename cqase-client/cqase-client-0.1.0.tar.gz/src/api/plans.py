from src.models import ResponseModel


class PlanesApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_PLANES = "/plan/{}"
    _POST_CREATE_PLANES = "/plan/{}"
    _GET_SPECIFIC_PLANES = "/plan/{}/{}"
    _DELETE_PLANES = "/plan/{}/{}"
    _UPDATE_PLANES = "/plan/{}/{}"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-plans
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_PLANES.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-plan
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_PLANES.format(code)}",
            json=body,
        )

    def get_specific_plane(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-plan
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}"
            f"{self._GET_SPECIFIC_PLANES.format(code, uuid)}",
        )

    def delete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-plan
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_PLANES.format(code, uuid)}",
        )

    def update(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-plan
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_PLANES.format(code, uuid)}",
            json=body,
        )
