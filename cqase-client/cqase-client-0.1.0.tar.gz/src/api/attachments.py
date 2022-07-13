import ntpath

from typing import Union, Tuple

from src.common.file_type import FileInfo
from src.models import ResponseModel


class AttachmentsApi:
    def __init__(self, app):
        self.app = app

    _GET_ALL_ATTACHMENTS = "/attachment"
    _POST_UPLOAD_ATTACHMENTS = "/attachment/{}"
    _GET_ATTACHMENTS_BY_HASH = "/attachment/{}"
    _DELETE_ATTACHMENTS_BY_HASH = "/attachment/{}"

    def upload(
        self,
        code: str,
        *file_infos: Union[str, Tuple[str, str], Tuple[bytes, str, str]],
    ) -> ResponseModel:
        """
        https://developers.qase.io/reference/upload-attachment
        """
        files = []
        for _id, file in enumerate(file_infos):
            filename, path, mime, content = FileInfo.get_file_info(file)
            files.append((str(_id), (filename or ntpath.basename(path), content, mime)))

        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_UPLOAD_ATTACHMENTS.format(code)}",
            files=files,
        )

    def get_all(self) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-attachments
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_ATTACHMENTS}",
        )

    def remove_by_hash(self, hash: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-attachment
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_ATTACHMENTS_BY_HASH.format(hash)}",
        )

    def get_by_hash(self, hash: str) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-attachment
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ATTACHMENTS_BY_HASH.format(hash)}",
        )
