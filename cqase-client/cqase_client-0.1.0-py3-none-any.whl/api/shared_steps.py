from src.models import ResponseModel


class SharedStepsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_SHARED_STEPS = "/shared_step/{}"
    _POST_CREATE_SHARED_STEP = "/shared_step/{}"
    _GET_SHARED_STEP_BY_CODE = "/shared_step/{}/{}"
    _DELETE_SHARED_STEP = "/shared_step/{}/{}"
    _UPDATE_SHARED_STEP = "/shared_step/{}/{}"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-shared-steps
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_SHARED_STEPS.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-shared-step
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_SHARED_STEP.format(code)}",
            json=body,
        )

    def delete(self, code: str, hash_shared_step: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-shared-step
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}"
            f"{self._DELETE_SHARED_STEP.format(code, hash_shared_step)}",
        )

    def get_specific_shared_step(
        self, code: str, hash_shared_step: str
    ) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-shared-step
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}"
            f"{self._GET_SHARED_STEP_BY_CODE.format(code, hash_shared_step)}",
        )

    def update(self, code: str, hash_shared_step: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-shared-step
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}"
            f"{self._UPDATE_SHARED_STEP.format(code, hash_shared_step)}",
            json=body,
        )
