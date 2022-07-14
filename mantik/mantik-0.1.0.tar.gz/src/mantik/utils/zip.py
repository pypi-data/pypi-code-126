import io
import os
import pathlib
import tempfile
import typing as t
import zipfile


def zip_directory(path: pathlib.Path) -> t.BinaryIO:
    """Zip given directory."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        with zipfile.ZipFile(tmp_dir + "/zip_tmp", "w") as zipwriter:
            for root, dirs, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)
                    zip_path = os.path.relpath(filepath, path)
                    zipwriter.write(filepath, zip_path)
            zipwriter.close()
        with open(tmp_dir + "/zip_tmp", "rb") as f:
            content = f.read()
        return io.BytesIO(content)
