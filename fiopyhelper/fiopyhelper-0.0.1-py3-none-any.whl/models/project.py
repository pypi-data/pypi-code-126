from __future__ import annotations

import json
from typing import TYPE_CHECKING

from fiopy.annotations.autowire import autowire
from fiopy.config import Config
from fiopy.enums import UserRole
from fiopy.http.http_request import HttpRequest
from fiopy.models.base import BaseModel
from fiopy.models.project_prefs import ProjectPrefsModel
from fiopy.models.project_root_folder import ProjectRootFolderModel
from fiopy.models.project_user_prefs import ProjectUserPrefsModel

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class ProjectModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._name = kwargs.get("name")
        self._description = kwargs.get("description")

        self._size = kwargs.get("size")

        self._team_id = kwargs.get("team_id")
        self._user_id = kwargs.get("user_id")
        self._root_folder_key = kwargs.get("root_folder_key")
        self._root_folder = None
        self._invite_url = kwargs.get("invite_url")

        self._archived_at = kwargs.get("archived_at")
        self._clear_from_usage = kwargs.get("clear_from_usage")
        self._ignore_archive = kwargs.get("ignore_archive")
        self._joinable = kwargs.get("joinable")
        self._private = kwargs.get("private")
        project_prefs = kwargs.get("project_prefs", {})
        while isinstance(project_prefs, str):
            project_prefs = json.loads(project_prefs)
        self._project_prefs = ProjectPrefsModel(**project_prefs)
        self._shared = kwargs.get("shared")
        self._slack_notifications_pref = kwargs.get("slack_notifications_pref")

        user_prefs = kwargs.get("user_prefs", {})
        while isinstance(user_prefs, str):
            user_prefs = json.loads(user_prefs)
        self._user_prefs = ProjectUserPrefsModel(**user_prefs)
        self._view_downloadable = kwargs.get("view_downloadable")
        self._view_only = kwargs.get("view_only")

        self._created_at_integer = kwargs.get("created_at_integer")
        self._updated_at_integer = kwargs.get("updated_at_integer")

        super().cleanup_values()

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def size(self):
        return self._size

    @property
    def team_id(self):
        return self._team_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def root_folder_key(self):
        return self._root_folder_key

    @property
    def root_folder(self):
        if not self._root_folder:
            self._root_folder = self._get_root_folder()
        return self._root_folder

    @root_folder.setter
    def root_folder(self, value):
        self._root_folder = value

    @property
    def invite_url(self):
        return self._invite_url

    @property
    def archived_at(self):
        return self._archived_at

    @property
    def clear_from_usage(self):
        return self._clear_from_usage

    @property
    def ignore_archive(self):
        return self._ignore_archive

    @property
    def joinable(self):
        return self._joinable

    @property
    def private(self):
        return self._private

    @property
    def project_prefs(self):
        return self._project_prefs

    @property
    def shared(self):
        return self._shared

    @property
    def slack_notifications_pref(self):
        return self._slack_notifications_pref

    @property
    def user_prefs(self):
        return self._user_prefs

    @property
    def view_downloadable(self):
        return self._view_downloadable

    @property
    def view_only(self):
        return self._view_only

    @property
    def created_at_integer(self):
        return self._created_at_integer

    @property
    def updated_at_integer(self):
        return self._updated_at_integer

    @autowire(argmap={"root_folder_id": "root_folder_key"})
    def _get_root_folder(self, root_folder_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_asset"])
            .add_path_param("asset_id", root_folder_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_model(model_clazz=ProjectRootFolderModel)

    def join(self, *, project_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["join_project"])
            .add_path_param("project_id", project_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response

    @autowire(argmap={"project_id": "id"})
    def leave(self, *, user_ids: list = None, project_id: str = None, user: UserModel = None):
        user_ids = user_ids or [user.id]
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["join_project"])
            .add_path_param("project_id", project_id)
            .set_header("Authorization", user.session_id)
            .body({"collaboratorIds": user_ids})
            .send()
        )

        return response

    @autowire(argmap={"project_id": "id"})
    def delete(self, *, project_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["delete_project"])
            .add_path_param("project_id", project_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.body().value(key="success").is_equal_to(True)

    def upload(self, *, file_path: str = None, folder_path: str = None, user: UserModel = None):
        return self.root_folder.upload(file_path=file_path, folder_path=folder_path, user=user)

    def get_children(self, *, asset_id: str = None, user: UserModel = None):
        return self.root_folder.get_children(asset_id=asset_id, user=user)

