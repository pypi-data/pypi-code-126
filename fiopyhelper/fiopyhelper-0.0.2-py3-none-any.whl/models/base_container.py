from __future__ import annotations

from typing import TYPE_CHECKING

from fiopy.config import Config
from fiopy.models.base import BaseModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class BaseContainerModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._item_count = kwargs.get("item_count")
        self._name = kwargs.get("name")
        self._created_at = kwargs.get("created_at_integer") or kwargs.get("inserted_at")
        self._updated_at = kwargs.get("updated_at_integer") or kwargs.get("updated_at")
        self._parent_id = kwargs.get("parent_id") or kwargs.get("owner_key")
        self._project_id = kwargs.get("project_id") or kwargs.get("project_key")
        self._private = kwargs.get("private", False)

    @property
    def item_count(self):
        return self._item_count

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def parent_id(self):
        return self._parent_id

    @property
    def project_id(self):
        return self._project_id

    @autowire(argmap={"asset_id": "id"})
    def get_children(self, *, asset_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_asset_children"])
            .add_path_param("asset_id", asset_id)
            .set_header("Authorization", user.session_id)
            .send()
        )
        from fiopy.models.asset import AssetModel

        return response.to_models(model_clazz=AssetModel)

