import os
from typing import Optional


def directory_last_edited(config_dir: str) -> Optional[float]:
    """Returns the last time a file or folder was edited in the given directory. None if folder doesn't exist."""
    if not os.path.exists(config_dir):
        return None
    last_edited = 0.0
    for path, folders, filenames in os.walk(config_dir):
        folders[:] = [folder for folder in folders if not folder.startswith(".")]
        for filename in filenames:
            if filename.endswith(".yml") or filename.endswith(".yaml"):
                last_edited = max(last_edited, os.path.getmtime(os.path.join(path, filename)))
        for folder in folders:
            last_edited = max(last_edited, os.path.getmtime(os.path.join(path, folder)))
    return last_edited
