from typing import TYPE_CHECKING

from fiopy.config import Config
from fiopy.models.base import BaseModel
from fiopy.annotations.autowire import autowire
from fiopy.http.http_request import HttpRequest
from fiopy.models.asset_impression import AssetImpression

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class ReviewLinkModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._allow_approvals = kwargs.get("allow_approvals")
        self._collaborators_and_team_members_ids = kwargs.get("collaborators_and_team_members_ids")
        self._created_at = kwargs.get("created_at")
        self._creator_key = kwargs.get("creator_key")
        self._current_version_only = kwargs.get("current_version_only")
        self._enable_downloading = kwargs.get("enable_downloading")
        self._expires_at = kwargs.get("expires_at")
        self._file_reference_keys = kwargs.get("file_reference_keys")
        self._file_references = kwargs.get("file_references")
        self._has_password = kwargs.get("has_password")
        self._is_active = kwargs.get("is_active")
        self._item_count = kwargs.get("item_count")
        self._master = kwargs.get("master")
        self._master_class = kwargs.get("master_class")
        self._name = kwargs.get("name")
        self._notify_on_view = kwargs.get("notify_on_view")
        self._owner = kwargs.get("owner")
        self._owner_id = kwargs.get("owner_id")
        self._password = kwargs.get("password")
        self._project_id = kwargs.get("project_key")
        self._account_id = kwargs.get("account_key")
        self._team_id = kwargs.get("team", {}).get("id")

        self._updated_at = kwargs.get("updated_at")
        self._user = kwargs.get("user")
        self._version_stack_keys = kwargs.get("version_stack_keys")
        self._version_stacks = kwargs.get("version_stacks")
        self._views_count = kwargs.get("views_count")

        super().cleanup_values()

    @property
    def allow_approvals(self):
        return self._allow_approvals

    @property
    def collaborators_and_team_members_ids(self):
        return self._collaborators_and_team_members_ids

    @property
    def created_at(self):
        return self._created_at

    @property
    def creator_key(self):
        return self._creator_key

    @property
    def current_version_only(self):
        return self._current_version_only

    @property
    def enable_downloading(self):
        return self._enable_downloading

    @property
    def expires_at(self):
        return self._expires_at

    @property
    def file_reference_keys(self):
        return self._file_reference_keys

    @property
    def file_references(self):
        return self._file_references

    @property
    def has_password(self):
        return self._has_password

    @property
    def is_active(self):
        return self._is_active

    @property
    def item_count(self):
        return self._item_count

    @property
    def master(self):
        return self._master

    @property
    def master_class(self):
        return self._master_class

    @property
    def name(self):
        return self._name

    @property
    def notify_on_view(self):
        return self._notify_on_view

    @property
    def owner(self):
        return self._owner

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def password(self):
        return self._password

    @property
    def project_id(self):
        return self._project_id

    @property
    def account_id(self):
        return self._account_id

    @property
    def team_id(self):
        return self._team_id

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def user(self):
        return self._user

    @property
    def version_stack_keys(self):
        return self._version_stack_keys

    @property
    def version_stacks(self):
        return self._version_stacks

    @property
    def views_count(self):
        return self._views_count

    @autowire(argmap={"review_link_id": "id"})
    def get_review_link_items(self, review_link_id: str = None, user: UserModel = None) -> list:
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_review_link_items"])
            .add_path_param("review_link_id", review_link_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_models(model_clazz=ReviewLinkModel)

