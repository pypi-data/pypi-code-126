"""File system utility."""
import os
from pathlib import Path
from typing import Union

PathLike = Union[str, bytes, os.PathLike]


def to_path(p: PathLike) -> Path:
    """Converts a PathLike path to a Path."""
    if isinstance(p, bytes):
        p = p.decode()
    return Path(p)


def create_dir(d_name: PathLike) -> None:
    """Creates a directory if it does not yet exist."""
    d_name_path = to_path(d_name)
    if not d_name_path.is_dir():
        d_name_path.mkdir(exist_ok=True)
