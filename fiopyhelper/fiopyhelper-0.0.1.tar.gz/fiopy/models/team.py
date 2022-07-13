from fiopy.config import Config
from fiopy.models.base import BaseModel
from fiopy.models.project import ProjectModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire
from fiopy.models.project_settings import ProjectSettings


class TeamModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._account_id = kwargs.get("account_id")
        self._allocation_data = kwargs.get("allocation_data")
        self._bio = kwargs.get("bio")
        self._created_at = kwargs.get("created_at")
        self._email_branding = kwargs.get("email_branding")
        self._max_collaborator = kwargs.get("max_collaborators")
        self._max_storage = kwargs.get("max_storage")
        self._member_limit = kwargs.get("member_limit")
        self._total_filesize = kwargs.get("total_filesize")
        self._avatar_url = kwargs.get("upload_url")
        self._watermark_text = kwargs.get("watermark")

        super().cleanup_values()

    @property
    def account_id(self):
        return self._account_id

    @property
    def allocation_data(self):
        return self._allocation_data

    @property
    def bio(self):
        return self._bio

    @property
    def created_at(self):
        return self._created_at

    @property
    def email_branding(self):
        return self._email_branding

    @property
    def max_collaborator(self):
        return self._max_collaborator

    @property
    def max_storage(self):
        return self._max_storage

    @property
    def member_limit(self):
        return self._member_limit

    @property
    def total_filesize(self):
        return self._total_filesize

    @property
    def avatar_url(self):
        return self._avatar_url

    @property
    def watermark_text(self):
        return self._watermark_text

    @autowire(argmap={"team_id": "id"})
    def get_projects(self, *, team_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["v1"]["endpoints"]["get_team_projects"])
            .set_header("Authorization", user.session_id)
            .add_path_param("team_id", team_id)
            .send()
        )

        return response.to_models(model_clazz=ProjectModel, key="projects")

    @autowire(argmap={"team_id": "id"})
    def create_project(self, *, team_id: str = None, settings: ProjectSettings = None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["create_project"])
            .set_header("Authorization", user.session_id)
            .add_path_param("team_id", team_id)
            .body(settings.settings)
            .send()
        )

        return response.to_model(model_clazz=ProjectModel, key="project")
