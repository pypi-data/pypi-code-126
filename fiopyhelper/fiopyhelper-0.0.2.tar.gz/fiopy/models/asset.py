from __future__ import annotations

from typing import TYPE_CHECKING

from fiopy.config import Config
from fiopy.models.base_asset import BaseAssetModel
from fiopy.models.comment import CommentModel
from fiopy.annotations.autowire import autowire
from fiopy.http.http_request import HttpRequest
from fiopy.models.asset_impression import AssetImpression

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class AssetModel(BaseAssetModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._archive_from = kwargs.get("archive_from")
        self._asset_type = kwargs.get("asset_type")
        self._cover = kwargs.get("cover")

        self._downloads = kwargs.get("downloads")

        self._frame_cover = kwargs.get("frame_cover")
        self._frame_custom = kwargs.get("frame_custom")
        self._frame_thumb = kwargs.get("frame_thumb")

        self._h264_1080_best = kwargs.get("h264_1080_best")
        self._h264_2160 = kwargs.get("h264_2160")
        self._h264_360 = kwargs.get("h264_360")
        self._h264_540 = kwargs.get("h264_540")
        self._h264_720 = kwargs.get("h264_720")
        self._hls_manifest = kwargs.get("hls_manifest")
        self._image_full = kwargs.get("image_full")
        self._image_high = kwargs.get("image_high")
        self._image_small = kwargs.get("image_small")
        self._includes = kwargs.get("includes")
        self._original = kwargs.get("original")
        self._original_upload = kwargs.get("original_upload")
        self._page_full = kwargs.get("page_full")
        self._page_high = kwargs.get("page_high")
        self._page_small = kwargs.get("page_small")
        self._required_transcodes = kwargs.get("required_transcodes")
        self._required_transcodes = kwargs.get("required_transcodes")
        self._sha256 = kwargs.get("sha256")
        self._source = kwargs.get("source")
        self._status = kwargs.get("status")
        self._thumb = kwargs.get("thumb")
        self._thumb_540 = kwargs.get("thumb_540")
        self._thumb_scrub = kwargs.get("thumb_scrub")
        self._transcode_statuses = kwargs.get("transcode_statuses")
        self._transcoded_at = kwargs.get("transcoded_at")
        self._transcodes = kwargs.get("transcodes")
        self._upload_completed_at = kwargs.get("upload_completed_at")
        self._upload_urls = kwargs.get("upload_urls")
        self._uploaded_at = kwargs.get("uploaded_at")
        self._versions = kwargs.get("versions")
        self._view_count = kwargs.get("view_count")
        self._webm_1080_best = kwargs.get("webm_1080_best")
        self._webm_360 = kwargs.get("webm_360")
        self._webm_540 = kwargs.get("webm_540")
        self._webm_720 = kwargs.get("webm_720")

        super().cleanup_values()

    @property
    def archive_from(self):
        return self._archive_from

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def cover(self):
        return self._cover

    @property
    def downloads(self):
        return self._downloads

    @property
    def frame_cover(self):
        return self._frame_cover

    @property
    def frame_custom(self):
        return self._frame_custom

    @property
    def frame_thumb(self):
        return self._frame_thumb

    @property
    def h264_1080_best(self):
        return self._h264_1080_best

    @property
    def h264_2160(self):
        return self._h264_2160

    @property
    def h264_360(self):
        return self._h264_360

    @property
    def h264_540(self):
        return self._h264_540

    @property
    def h264_720(self):
        return self._h264_720

    @property
    def hls_manifest(self):
        return self._hls_manifest

    @property
    def image_full(self):
        return self._image_full

    @property
    def image_high(self):
        return self._image_high

    @property
    def image_small(self):
        return self._image_small

    @property
    def includes(self):
        return self._includes

    @property
    def original(self):
        return self._original

    @property
    def original_upload(self):
        return self._original_upload

    @property
    def page_full(self):
        return self._page_full

    @property
    def page_high(self):
        return self._page_high

    @property
    def page_small(self):
        return self._page_small

    @property
    def required_transcodes(self):
        return self._required_transcodes

    @property
    def sha256(self):
        return self._sha256

    @property
    def source(self):
        return self._source

    @property
    def status(self):
        return self._status

    @property
    def thumb(self):
        return self._thumb

    @property
    def thumb_540(self):
        return self._thumb_540

    @property
    def thumb_scrub(self):
        return self._thumb_scrub

    @property
    def transcode_statuses(self):
        return self._transcode_statuses

    @property
    def transcoded_at(self):
        return self._transcoded_at

    @property
    def transcodes(self):
        return self._transcodes

    @property
    def upload_completed_at(self):
        return self._upload_completed_at

    @property
    def upload_urls(self):
        return self._upload_urls

    @property
    def uploaded_at(self):
        return self._uploaded_at

    @property
    def versions(self):
        return self._versions

    @property
    def view_count(self):
        return self._view_count

    @property
    def webm_1080_best(self):
        return self._webm_1080_best

    @property
    def webm_360(self):
        return self._webm_360

    @property
    def webm_540(self):
        return self._webm_540

    @property
    def webm_720(self):
        return self._webm_720

    @autowire(argmap={"asset_id": "id"})
    def delete_asset(self, *, asset_id: str = None, user: UserModel = None) -> bool:
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .delete(Config.api["v2"]["endpoints"]["batch_assests"])
            .set_header("Authorization", user.session_id)
            .body({"batch": [{"id": asset_id}]})
            .send()
        )

        return response.body().value(key="error").is_empty()

    @autowire(argmap={"asset_id": "id"})
    def get_impressions(self, *, asset_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_asset_impressions"])
            .add_path_param("asset_id", asset_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_models(model_clazz=AssetImpression)

    @autowire(argmap={"asset_id": "id"})
    def get_comments(self, *, asset_id: str = None, user: UserModel = None) -> CommentModel:
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["asset_comments"])
            .add_path_param("asset_id", asset_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_models(model_clazz=CommentModel)

    @autowire(argmap={"asset_id": "id"})
    def create_comment(
        self,
        *,
        annotation: str = None,
        text: str = None,
        private: bool = False,
        timestamp: str = None,
        page: int = None,
        asset_id: str = None,
        user: UserModel = None,
    ) -> CommentModel:
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .post(Config.api["v2"]["endpoints"]["asset_comments"])
            .add_path_param("asset_id", asset_id)
            .set_header("Authorization", user.session_id)
            .body({"annotation": annotation, "text": text, "private": private, "timestamp": timestamp, "page": page})
            .send()
        )

        return response.to_model(model_clazz=CommentModel)

