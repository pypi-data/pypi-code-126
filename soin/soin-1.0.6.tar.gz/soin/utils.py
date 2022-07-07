import functools
import logging
import os
import random
import shutil
import signal
import sys
import time
import requests
import tempfile
from pathlib import Path

from soin.job import SpiderJob


class TestJob(SpiderJob):

    def on_success(self):
        pass

    def on_failed(self):
        pass

    def perform(self):
        logging.info("test job is running")
        if random.random() < 0.3:
            logging.error("test job exception occued")
            raise Exception("test exception from test job")
        return 1


def while_true(interval=1):
    def decorator(func):
        @functools.wraps(func)
        def __inner(self, *args, **kwargs):
            while True:
                if self.stop:
                    break
                func(self, *args, **kwargs)
                time.sleep(interval)

        return __inner

    return decorator


def setup_root(root: str) -> Path:
    path = Path(root)
    path.mkdir(exist_ok=True, parents=True)
    return path


def setup_logger(log_file, level=logging.INFO):
    stdout_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(filename=log_file)

    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        handlers=[file_handler, stdout_handler],
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
            logging.warn(
                f"download file from {url} failed for {i+1} time, exception: {e}"
            )
    else:
        logging.error(
            f"download file from {url} failed after {i + 1}, quit"
        )
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


def retry(count: int):
    def decorator(func):
        @functools.wraps(func)
        def real_func(*args, **kwargs):
            for i in range(count):
                try:
                    res = func(*args, **kwargs)
                    break
                except Exception as e:
                    logging.exception(
                        f"call func {func.__name__} failed for {i} time, exception {e}"
                    )
                    time.sleep(1 + i)
            else:
                logging.error(
                    f"call func {func.__name__} failed after {count} time"
                )
                return None
            return res

        return real_func

    return decorator
