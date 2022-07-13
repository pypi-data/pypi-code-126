from src.models import ResponseModel


class DefectsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_DEFECTS = "/defect/{}"
    _POST_CREATE_NEW_DEFECTS = "/defect/{}"
    _GET_SPECIFIC_DEFECTS = "/defect/{}/{}"
    _DELETE_DEFECTS = "/defect/{}/{}"
    _UPDATE_DEFECTS = "/defect/{}/{}"
    _UPDATE_RESOLVE_DEFECT = "/defect/{}/resolve/{}"
    _UPDATE_DEFECT_STATUS = "/defect/{}/status/{}"

    def get_all(self, code: str):
        """
        https://developers.qase.io/reference/get-defects
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_DEFECTS.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-defect
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_NEW_DEFECTS.format(code)}",
            json=body,
        )

    def get_specific_defect(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-defect
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_SPECIFIC_DEFECTS.format(code, uuid)}",
        )

    def delete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-defect
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_DEFECTS.format(code, uuid)}",
        )

    def update(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-defect
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_DEFECTS.format(code, uuid)}",
            json=body,
        )

    def resolve_defect(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/resolve-defect
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_RESOLVE_DEFECT.format(code, uuid)}",
        )

    def update_status(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-defect-status
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_DEFECT_STATUS.format(code, uuid)}",
            json=body,
        )
