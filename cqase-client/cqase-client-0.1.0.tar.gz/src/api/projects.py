from src.models import ResponseModel


class ProjectsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_PROJECTS = "/project"
    _POST_CREATE_NEW_PROJECT = "/project"
    _GET_PROJECT_BY_CODE = "/project/{}"
    _DELETE_PROJECT_BY_CODE = "/project/{}"
    _POST_GRANT_ACCESS_PROJECT = "/project/{}/access"
    _DELETE_REVOKE_ACCESS_PROJECT = "/project/{}/access"

    def get_all(self) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-projects
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_PROJECTS}",
        )

    def create(self, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-project
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_NEW_PROJECT}",
            json=body,
        )

    def delete(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-project
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_PROJECT_BY_CODE.format(code)}",
        )

    def get_project_by_code(self, code: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-project
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_PROJECT_BY_CODE.format(code)}",
        )

    def grand_access(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/grant-access-to-project
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_GRANT_ACCESS_PROJECT.format(code)}",
            json=body,
        )

    def revoke_access(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/revoke-access-to-project
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}"
            f"{self._DELETE_REVOKE_ACCESS_PROJECT.format(code)}",
            json=body,
        )
