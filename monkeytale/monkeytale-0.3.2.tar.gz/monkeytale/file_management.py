"""Utilities to manage monkeytale file storage."""

import shutil
from pathlib import Path

from eliot import current_action, log_call, to_file
from eliot.json import EliotJSONEncoder

BUILD_DIRECTORY = "build"
LOG_FILE = "monkeytale.log"


source_path = Path(".")
log_path = source_path / LOG_FILE
build_path = source_path / BUILD_DIRECTORY


class MonkeytaleJSONEncoder(EliotJSONEncoder):
    def default(self, obj):  # pragma: no cover
        try:
            encoded_value = EliotJSONEncoder.default(self, obj)
        except TypeError:
            encoded_value = repr(obj)

        return encoded_value


def start_log():
    # Always overwrite the log for each run
    to_file(log_path.open(mode="w"), encoder=MonkeytaleJSONEncoder)


@log_call
def initialize_build_directory():
    # Build from scratch every time
    if build_path.is_dir():
        current_action().log(
            message_type=f"Deleting previous '{BUILD_DIRECTORY}' directory",
            path=str(build_path.resolve()),
        )
        shutil.rmtree(build_path)
    build_path.mkdir(exist_ok=False, parents=True)
    return str(build_path)
