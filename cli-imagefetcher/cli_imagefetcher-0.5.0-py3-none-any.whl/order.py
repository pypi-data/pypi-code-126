import os, time, json, requests, pathlib

from requests.auth import HTTPBasicAuth
from .CONSTANTS import *


def orderApiRequest(apikey, featureIdArray):
    auth = HTTPBasicAuth(apikey, "")
    orderRequest = formatRequest(auth, featureIdArray)
    orderId = orderRequest.json()["id"]
    orderUrl = ORDER_API_ENDPOINT + "/" + orderId
    awaitOrder(orderUrl, auth)
    downloadPaths = getOrder(orderUrl, auth)
    return downloadPaths


def formatRequest(auth, idArray):
    headers = {"content-type": "application/json"}
    request = {
        "delivery": {"single_archive": True, "archive_type": "zip"},
        "name": "test order",
        "products": [
            {
                "item_ids": idArray,
                "item_type": ITEM_TYPE,
                "product_bundle": ORDER_PRODUCT_BUNDLE,
            }
        ],
    }
    response = requests.post(
        ORDER_API_ENDPOINT,
        data=json.dumps(request),
        auth=auth,
        headers=headers,
    )
    return response


def awaitOrder(orderUrl, auth, numLoops=40):
    count = 0
    while count < numLoops:
        count += 1
        r = requests.get(orderUrl, auth=auth)
        response = r.json()
        state = response["state"]
        print(state)
        endStates = ["success", "failed"]
        if state in endStates:
            break
        time.sleep(10)


def getOrder(orderUrl, auth):
    r = requests.get(orderUrl, auth=auth)
    response = r.json()
    results = response["_links"]["results"]
    pathsArray = downloadData(results)
    return pathsArray


def downloadData(results, overwrite=False):
    paths = []
    results_urls = [r["location"] for r in results]
    results_names = [r["name"] for r in results]
    print("{} items to download".format(len(results_urls)))
    for url, name in zip(results_urls, results_names):
        path = pathlib.Path(os.path.join(OUT_DIRECTORY, name))

        if overwrite or not path.exists():
            print("downloading {} to {}".format(name, path))
            r = requests.get(url, allow_redirects=True)
            path.parent.mkdir(parents=True, exist_ok=True)
            open(path, "wb").write(r.content)
            paths.append(path)
        else:
            print("{} already exists, skipping {}".format(path, name))
    return paths
