from __future__ import annotations

import os
import random
from typing import TYPE_CHECKING

from fiopy.config import Config
from fiopy.models.asset import AssetModel
from fiopy.models.base_container import BaseContainerModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire
from magic import Magic

if TYPE_CHECKING:
    from fiopy.models.user import UserModel


class BaseFolderModel(BaseContainerModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._cover_asset_id = kwargs.get("cover_asset_id")
        self._index = kwargs.get("index")
        self._shared = kwargs.get("shared")

        self._recent_asset = None
        self._recent_review_link = None

    @property
    def cover_asset_id(self):
        return self._cover_asset_id

    @property
    def index(self):
        return self._index

    @property
    def shared(self):
        return self._shared

    @property
    def recent_asset(self):
        return self._recent_asset

    @property
    def recent_review_link(self):
        return self._recent_review_link

    def upload(self, *, file_path: str = None, folder_path: str = None, folder_id: str = None, user: UserModel = None):

        models = []
        if file_path:
            model = self._create_asset_holder(file_path=file_path, folder_id=folder_id, user=user)
            models.append(model)
        elif folder_path:
            for dir_path, _, files in os.walk(folder_path, topdown=False):
                for fil in files:
                    model = self._create_asset_holder(
                        file_path=os.path.join(dir_path, fil), folder_id=folder_id, user=user
                    )
                    # BaseFolderModel._upload(
                    #     file_path=os.path.join(dir_path, fil), model=model
                    # )
                    if model:
                        models.append(model)
        return models

    @autowire(argmap={"folder_id": "id"})
    def _create_asset_holder(self, *, file_path: str = None, folder_id: str = None, user: UserModel = None):
        file_path = os.path.abspath(file_path)
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .post(Config.api["v2"]["endpoints"]["upload_asset"])
            .add_path_param("folder_id", folder_id)
            .set_header("Authorization", user.session_id)
            .body(
                {
                    "type": "file",
                    "name": os.path.basename(file_path),
                    "filetype": Magic(mime=True).from_file(file_path),
                    "filesize": os.path.getsize(file_path),
                    "index": random.randint(1, 100000) * -1,
                }
            )
            .send()
        )

        return response.to_model(model_clazz=AssetModel)

    @staticmethod
    def _upload(*, file_path: str = None, model: AssetModel = None):
        file_path = os.path.abspath(file_path)
        with open(file_path, "rb") as fil:
            upload_url = model.upload_urls[0]
            s3_upload_hostname = "/".join(upload_url.split("/")[:3])
            upload_url = "/" + "/".join(upload_url.split("/")[3:])
            HttpRequest.request(s3_upload_hostname).put(upload_url).set_header("x-amz-acl", "private").attach(
                fil
            ).send()

            print(HttpRequest._last_response)

    @autowire()
    def get_asset(self, *, asset_id: str = None, user: UserModel = None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["get_asset"])
            .add_path_param("asset_id", asset_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_model(model_clazz=AssetModel)
