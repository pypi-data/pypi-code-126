import os
from google.cloud import storage

from . import git
from .exceptions import LoggedError

BUCKET = storage.Client().bucket("aaa-terraform-state")


class PlanNotFound(LoggedError):
    def __init__(self, obj: str) -> None:
        super().__init__(f"Could not find plan object {obj}")


def upload(workspace: str, filename: str) -> None:
    blobname = _blobname(workspace, filename)
    blob = BUCKET.blob(blobname)
    blob.upload_from_filename(filename)
    print(f"Uploaded plan to gs://{blob.bucket.name}/{blob.name}")


def download(workspace: str, filename: str) -> None:
    blobname = _blobname(workspace, filename)
    blob = BUCKET.get_blob(blobname)
    if not blob:
        raise PlanNotFound(blobname)
    blob.download_to_filename(filename)
    print(f"Downloaded plan to gs://{blob.bucket.name}/{blob.name}")


def _blobname(workspace: str, filename: str) -> str:
    basename = os.path.basename(filename)
    repo = git.get_repo_name()
    return f"{repo}/plans/{workspace}/{basename}"
