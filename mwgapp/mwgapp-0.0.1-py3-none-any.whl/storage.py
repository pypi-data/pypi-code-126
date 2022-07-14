from .exceptions import LoggedError

BUCKET = "aaa-terraform-state"


class StorageObjectNotFoundError(LoggedError):
    def __init__(self, obj: str) -> None:
        super().__init__(f"Could not find storage object {obj}")


def upload(obj: str) -> None:
    print("Uploading:", obj)


def download(obj: str) -> None:
    raise StorageObjectNotFoundError(obj)
