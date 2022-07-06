import functools
import logging
import os
import shutil
import requests
import tempfile
from pathlib import Path


def setup_root(root: str) -> Path:
    path = Path(root)
    path.mkdir(exist_ok=True, parents=True)
    return path


def setup_logger(log_file, level=logging.INFO):
    logging.basicConfig(
        filename=log_file,
        level=level,
        format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )


def download_file(url: str, dest: str = None) -> bytes:
    fp = tempfile.NamedTemporaryFile(delete=False)
    for i in range(5):
        fp.seek(0)
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1024**2):
                    fp.write(chunk)
            break
        except Exception as e:
            logging.warn(f"download file from {url} failed for {i+1} time, exception: {e}")
    else:
        logging.error(f"download file from {url} failed after {i + 1} time, last exception is {e}")
        fp.close()
        os.remove(fp.name)
        raise e
    if dest is None:
        fp.seek(0)
        bytes = fp.read()
        fp.close()
        os.remove(fp.name)
        return bytes
    else:
        fp.close()
        shutil.copy(fp.name, dest)
        os.remove(fp.name)
        return None


def retry(time: int):

    def decorator(func):

        @functools.wraps(func)
        def real_func(*args, **kwargs):
            for i in range(time):
                try:
                    res = func(*args, **kwargs)
                    break
                except Exception as e:
                    logging.warn(f"call func {func.__name__} failed for {i} time, exception {e}")
                    time.sleep(1 + i)
            else:
                logging.error(f"call func {func.__name__} failed after {time} time, last exception {e}")
                raise e
            return res

        return real_func

    return decorator
