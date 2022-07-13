from src.models import ResponseModel


class CustomFieldsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_FIELDS = "/custom_field"
    _POST_NEW_FIELDS = "/custom_field"
    _GET_CUSTOM_FIELDS_BY_ID = "/custom_field/{}"
    _DELETE_CUSTOM_FIELDS = "/custom_field/{}"
    _UPDATE_CUSTOM_FIELDS = "/custom_field/{}"

    def get_all(self, params: dict = None) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-custom-fields
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_FIELDS}",
            params=params,
        )

    def create(self, body: dict):
        """
        https://developers.qase.io/reference/create-custom-field
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_NEW_FIELDS}",
            json=body,
        )

    def get_by_id(self, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-custom-field
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_CUSTOM_FIELDS_BY_ID.format(uuid)}",
        )

    def delete(self, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-custom-field
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_CUSTOM_FIELDS.format(uuid)}",
        )

    def update(self, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-custom-field
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_CUSTOM_FIELDS.format(uuid)}",
            json=body,
        )
