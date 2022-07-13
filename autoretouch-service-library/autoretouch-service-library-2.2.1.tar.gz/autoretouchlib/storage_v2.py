import logging
import os
from typing import Union, Optional

import httpx
import google
from google.auth.transport.requests import Request as GoogleAuthRequest
from google.oauth2.id_token import fetch_id_token
from fastapi import HTTPException

from autoretouchlib.auth import get_id_token
from autoretouchlib.types import FileContentHash, OrganizationId, FileType


class Storage:
    def __init__(self):
        self.url = os.getenv("STORAGE_SERVICE_URL", "http://0.0.0.0:8180") + "/image/"
        try:
            self.id_token = get_id_token(self.url)
        except RuntimeError:
            self.id_token = None
        self.client = httpx.Client(http2=True, timeout=httpx.Timeout(None, read=300, write=300))

    def load(self, content_hash: Union[FileContentHash, str], organization_id: OrganizationId
             ) -> bytes:
        if isinstance(content_hash, str):
            content_hash = FileContentHash(content_hash)
        headers = {} if not self.id_token else {"Authorization": f"Bearer {self.id_token}"}
        params = {
            "organization_id": organization_id,
            "content_hash": content_hash.get_value()
        }
        response = self.client.get(self.url, params=params, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail=f"could not load image from storage: {response.content.decode('utf-8')}")
        content_length = response.headers.get("Content-Length", response.headers.get("X-Content-Length"))
        if content_length is None:
            raise HTTPException(status_code=500,
                                detail=f"No content-length header received when requesting {organization_id}/{content_hash}")
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

        headers = {} if not self.id_token else {"Authorization": f"Bearer {self.id_token}"}
        params = {
            "organization_id": organization_id,
            "content_hash": content_hash.get_value(),
            "content_type": content_type.value
        }
        response = self.client.post(self.url, params=params, content=blob, headers=headers)
        if response.status_code not in (200, 201):
            logging.warning(response.status_code, response.content.decode('utf-8'))
            raise HTTPException(status_code=response.status_code,
                                detail=f"could not load store file: {response.content.decode('utf-8')}")
        assert response.json()["contentHash"] == content_hash.get_value()
        return content_hash


storage = Storage()
