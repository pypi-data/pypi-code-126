import os
from pathlib import Path


def get_command_output(command: str) -> str:
    return os.popen(command).read().strip()


def relative_to_absolute(relative_path: str) -> str:
    return (
        Path(os.getcwd(), relative_path).__str__()
        if not relative_path.startswith("/")
        else relative_path
    )
