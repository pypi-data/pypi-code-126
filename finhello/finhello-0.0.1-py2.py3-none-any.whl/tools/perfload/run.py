import logging
import socket
from concurrent.futures import ThreadPoolExecutor

import requests
import requests.packages.urllib3.util.connection as urllib3_cn

from utils import log_timing

logger = logging.getLogger(__name__)


def allowed_gai_family_custom():
    """
    Done based on https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request
    Original sources for allowed_gai_family in https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    """
    return socket.AF_INET


urllib3_cn.allowed_gai_family = allowed_gai_family_custom


@log_timing
def call_endpoint(uri, payload):
    r = requests.post(uri, data={'key': 'value'})
    # print(r)
    # print(r.text)
    return r


def main():
    # e = ThreadPoolExecutor(max_workers=50)
    # futures = [
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    #     e.submit(call_endpoint, "http://localhost:5000", {}),
    # ]


    # future.result()


    # with ThreadPoolExecutor(max_workers=50) as executor:
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #     future = executor.submit(call_endpoint, "http://localhost:5000", {})
    #
    #
    #     print(future.result())

    # with ThreadPoolExecutor(max_workers=50) as executor:
    #     tasks = ["http://localhost:5000"] * 5
    #     futures = executor.map(call_endpoint, tasks)
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    resp = call_endpoint("http://localhost:5000", {})

    # main()

