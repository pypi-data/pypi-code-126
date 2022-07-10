import hashlib
import logging
import os
import shutil
import time
from urllib.parse import urlparse

import requests

from corlyutils.logging_helper import config_my_log

logger = logging.getLogger(__name__)
requests.packages.urllib3.disable_warnings()


def send_notice(content):
    requests.post("http://192.168.31.5:99/i/wechat/send-notice", json={"content": content})


def try_get(max_try, url, headers=None, proxies=None, stream=None):
    for i in range(max_try):
        try:
            resp = requests.get(url, headers=headers, proxies=proxies, verify=False, stream=stream, timeout=60)
            if resp.status_code == 200:
                return resp
            else:
                msg = "url {} status_code {} resp {}".format(url, resp.status_code, resp.text)
                logger.info(msg)
                send_notice(msg)
                if i == max_try - 1:
                    return resp
        except Exception as e:
            logger.info("http_util sleep 10s i %d %s", i, e)
            time.sleep(10)
    send_notice("url {} retryMax {} 仍然没有获取到数据", url, max_try)


def download_file(url, local_dir, headers=None, proxies=None, override=False):
    url_parse = urlparse(url)
    filepath = local_dir + url_parse.path
    if not override and os.path.exists(filepath):
        logger.warning("download_file 文件已存在 %s", filepath)
        return filepath, url_parse.path, True
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    resp = try_get(4, url, headers, proxies, stream=True)
    if resp.status_code == 200:
        with open(filepath, 'wb') as f:
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, f)
    logger.info('download_file status_code %s %s', resp.status_code, filepath)
    return filepath, url_parse.path, False


def file_info(filepath):
    with open(filepath, 'rb') as f:
        md5 = hashlib.md5(f.read())
    return os.path.getsize(filepath), md5.hexdigest()


def read_headers(path):
    headers = {}
    with open(path) as f:
        lines = f.read().splitlines()
        for line in lines:
            idx = line.find(':')
            headers[line[:idx]] = line[idx + 1:]
    return headers


if __name__ == '__main__':
    config_my_log("http_util")
    resp = try_get(3, "http://192.168.31.9:99/i/wechat/send-notice1")
    print(resp)
