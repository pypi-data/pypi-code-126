import os
import shutil

import requests
from tqdm.auto import tqdm


def download(url: str, save_path: str):
    with requests.get(url, stream=True) as r:
        total_length = int(r.headers.get("Content-Length"))
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
            with open(save_path, "wb") as output:
                shutil.copyfileobj(raw, output)


if __name__ == "__main__":
    save_path = "./test_download.docx"
    download(
        "https://file-examples.com/wp-content/uploads/2017/02/file-sample_1MB.docx",
        save_path,
    )
    os.remove(save_path)
