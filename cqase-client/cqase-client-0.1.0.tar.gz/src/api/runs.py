from src.models import ResponseModel


class RunsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_RUNS = "/run/{}"
    _POST_CREATE_RUNS = "/run/{}"
    _GET_SPECIFIC_RUNS = "/run/{}/{}"
    _DELETE_RUNS = "/run/{}/{}"
    _UPDATE_RUNS = "/run/{}/{}/public"
    _POST_COMPLETE_RUNS = "/run/{}/{}/complete"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-runs
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_RUNS.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-run
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_RUNS.format(code)}",
            json=body,
        )

    def get_run(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-run
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}" f"{self._GET_SPECIFIC_RUNS.format(code, uuid)}",
        )

    def delete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-run
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_RUNS.format(code, uuid)}",
        )

    def update(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-run-publicity
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_RUNS.format(code, uuid)}",
            json=body,
        )

    def complete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/complete-run
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_COMPLETE_RUNS.format(code, uuid)}",
        )
