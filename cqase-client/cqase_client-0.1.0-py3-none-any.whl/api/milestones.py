from src.models import ResponseModel


class MilestoneApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_MILESTONES = "/milestone/{}"
    _POST_CREATE_MILESTONES = "/milestone/{}"
    _GET_SPECIFIC_MILESTONES = "/milestone/{}/{}"
    _DELETE_MILESTONES = "/milestone/{}/{}"
    _UPDATE_MILESTONES = "/milestone/{}/{}"

    def get_all(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-milestones
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_MILESTONES.format(code)}",
        )

    def create(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-milestone
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_MILESTONES.format(code)}",
            json=body,
        )

    def get_specific_milestone(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-milestone
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}"
            f"{self._GET_SPECIFIC_MILESTONES.format(code, uuid)}",
        )

    def delete(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-milestone
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_MILESTONES.format(code, uuid)}",
        )

    def update(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-milestone
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_MILESTONES.format(code, uuid)}",
            json=body,
        )
