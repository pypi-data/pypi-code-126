from __future__ import annotations

from typing import TYPE_CHECKING

from fiopy.config import Config
from fiopy.models.base import BaseModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class CommentModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._anonymous_user_id = kwargs.get("anonymous_user_id")
        self._asset_id = kwargs.get("asset_id")

        self._comment_entities = kwargs.get("comment_entities")
        self._completed_at = kwargs.get("completed_at")
        self._completer_id = kwargs.get("completer_id")

        self._annotation = kwargs.get("annotation")
        self._aspect_ratio = kwargs.get("aspect_ratio")
        self._duration = kwargs.get("duration")

        self._deleted_at = kwargs.get("deleted_at")
        self._fov = kwargs.get("fov")
        self._has_replies = kwargs.get("has_replies")
        self._inserted_at = kwargs.get("inserted_at")
        self._like_count = kwargs.get("like_count")
        self._owner_id = kwargs.get("owner_id")
        self._page = kwargs.get("page")
        self._parent_id = kwargs.get("parent_id")
        self._pitch = kwargs.get("pitch")
        self._private = kwargs.get("private")
        self._read_count = kwargs.get("read_count")
        self._review_link_id = kwargs.get("review_link_id")
        self._text = kwargs.get("text")
        self._thumb = kwargs.get("thumb")
        self._timestamp = kwargs.get("timestamp")
        self._updated_at = kwargs.get("updated_at")
        self._yaw = kwargs.get("yaw")

        super().cleanup_values()

    @property
    def anonymous_user_id(self):
        return self._anonymous_user_id

    @property
    def asset_id(self):
        return self._asset_id

    @property
    def comment_entities(self):
        return self._comment_entities

    @property
    def completed_at(self):
        return self._completed_at

    @property
    def completer_id(self):
        return self._completer_id

    @property
    def annotation(self):
        return self._annotation

    @property
    def aspect_ratio(self):
        return self._aspect_ratio

    @property
    def duration(self):
        return self._duration

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def fov(self):
        return self._fov

    @property
    def has_replies(self):
        return self._has_replies

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def like_count(self):
        return self._like_count

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def page(self):
        return self._page

    @property
    def parent_id(self):
        return self._parent_id

    @property
    def pitch(self):
        return self._pitch

    @property
    def private(self):
        return self._private

    @property
    def read_count(self):
        return self._read_count

    @property
    def review_link_id(self):
        return self._review_link_id

    @property
    def text(self):
        return self._text

    @property
    def thumb(self):
        return self._thumb

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def yaw(self):
        return self._yaw

    @autowire(argmap={"comment_id": "id"})
    def get_replies(self, *, comment_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["comment_replies"])
            .add_path_param("comment_id", comment_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_models(model_clazz=CommentModel)

    @autowire(argmap={"comment_id": "id"})
    def reply(
        self,
        *,
        annotation: str = None,
        text: str = None,
        private: bool = None,
        timestamp: str = None,
        page: str = None,
        comment_id: str = None,
        user: UserModel = None,
    ):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .post(Config.api["v2"]["endpoints"]["comment_replies"])
            .add_path_param("comment_id", comment_id)
            .set_header("Authorization", user.session_id)
            .body({"annotation": annotation, "text": text, "private": private, "timestamp": timestamp, "page": page})
            .send()
        )

        return response.to_model(model_clazz=CommentModel)
