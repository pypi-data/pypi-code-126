import logging
import os
from typing import Union, Optional

from google.auth.transport.requests import Request as GoogleAuthRequest
from google.oauth2.id_token import fetch_id_token
import requests
from fastapi import HTTPException

from autoretouchlib.types import FileContentHash, OrganizationId, FileType


class Storage:
    def __init__(self):
        self.url = os.getenv("STORAGE_SERVICE_URL", "http://0.0.0.0:8180/") + "image/"

    def __get_id_token(self) -> Optional[str]:
        try:
            auth_req = GoogleAuthRequest()
            id_token = fetch_id_token(auth_req, self.url)
            return id_token
        except Exception as e:
            logging.warning(f"Could not fetch IdToken for {self.url}: {e}")
            return None

    def load(self, content_hash: Union[FileContentHash, str], organization_id: OrganizationId
             ) -> bytes:
        if isinstance(content_hash, str):
            content_hash = FileContentHash(content_hash)
        id_token = self.__get_id_token()
        headers = {} if not id_token else {"Authorization": f"Bearer {id_token}"}
        params = {
            "organization_id": organization_id,
            "content_hash": content_hash.get_value()
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail=f"could not load image from storage: {response.content.decode('utf-8')}")
        content_length = response.headers.get("Content-Length", response.headers.get("X-Content-Length"))
        if content_length is None:
            raise HTTPException(status_code=500, detail=f"No content-length header received when requesting {organization_id}/{content_hash}")
        else:
            logging.debug(f"len(content): {len(response.content)}, content_length: {content_length}")
            if len(response.content) != int(content_length):
                raise HTTPException(status_code=500,
                                    detail=f"response was truncated: expected {int(content_length)} bytes, "
                                           f"received {len(response.content)} bytes")
        return response.content

    def store(self, blob: bytes, content_type: Union[FileType, str], organization_id: OrganizationId
              ) -> FileContentHash:
        if isinstance(content_type, str):
            content_type = FileType(content_type)
        content_hash = FileContentHash.from_bytes(blob)

        id_token = self.__get_id_token()
        headers = {} if not id_token else {"Authorization": f"Bearer {id_token}"}
        params = {
            "organization_id": organization_id,
            "content_hash": content_hash.get_value(),
            "content_type": content_type.value
        }
        response = requests.post(self.url, params=params, data=blob, headers=headers)
        if response.status_code not in (200, 201):
            raise HTTPException(status_code=response.status_code,
                                detail=f"could not load store file: {response.content.decode('utf-8')}")
        assert response.json()["contentHash"] == content_hash.get_value()
        return content_hash


storage = Storage()
