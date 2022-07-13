from src.models import ResponseModel


class ResultsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_RESULTS = "/result/{}"
    _POST_CREATE_RESULTS = "/result/{}/{}"
    _GET_SPECIFIC_RESULTS = "/result/{}/{}"
    _DELETE_RESULTS = "/result/{}/{}/{}"
    _UPDATE_RESULTS = "/result/{}/{}/{}"
    _POST_BULK_RESULTS = "/result/{}/{}/bulk"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-results
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_RESULTS.format(code)}",
        )

    def create(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-result
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_RESULTS.format(code, uuid)}",
            json=body,
        )

    def get_result(self, code: str, hash_result: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-result
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}"
            f"{self._GET_SPECIFIC_RESULTS.format(code, hash_result)}",
        )

    def delete(self, code: str, uuid: int, hash_result: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-result
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}"
            f"{self._DELETE_RESULTS.format(code, uuid, hash_result)}",
        )

    def update(
        self, code: str, uuid: int, hash_result: str, body: dict
    ) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-result
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}"
            f"{self._UPDATE_RESULTS.format(code, uuid, hash_result)}",
            json=body,
        )

    def bulk(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-result-bulk
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_BULK_RESULTS.format(code, uuid)}",
            json=body,
        )
