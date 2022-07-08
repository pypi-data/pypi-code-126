import json
import threading

import requests
import pandas as pd

from .config import Config
from .checker import Checker


class Client(object):
    _threading_local = threading.local()

    def __init__(self):
        self.host = Config.host
        self.port = Config.port
        self._refresh_token = None
        self._access_token = None
        self._instance = None
        self.root_url = f'http://{self.host}:{self.port}/api/v1/'

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            _instance = Client()
            cls._threading_local._instance = _instance
        return _instance

    def _make_url(self, param):
        resource_url = f'{param.get("domain")}/{param.get("phylum")}/{param.get("class")}'
        return self.root_url + resource_url

    def _make_qeury_param(self, param):
        q = {k: v for k, v in param.items() if k not in ["domain", "phylum", "class"]}
        return q

    def _query(self, param):
        url = self._make_url(param)
        query_param = self._make_qeury_param(param)
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        r = requests.post(url, json=query_param, headers=headers)
        return r

    def _login(self, username, password, refresh=True):
        url = f'{self.root_url}/security/login'
        if refresh:
            body = {
                "username": username,
                "password": password,
                "provider": 'db',
                "refresh": True
            }
        else:
            body = {
                "username": username,
                "password": password,
                "provider": 'db'
            }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(url, data=json.dumps(body), headers=headers)
        return r

    def _refresh(self, refresh_token):
        url = f"{self.root_url}/security/refresh"
        headers = {
            "Authorization": f'Bearer {refresh_token}'
        }
        r = requests.post(url, headers=headers)
        return r

    def login(self, username, password):
        r = self._login(username, password, refresh=False)
        if r.status_code == 200:
            # login succeed
            result = r.json()
            self._access_token = result['access_token']
        elif r.status_code == 401:
            result = r.json()
            raise Exception(f"Login failed, ret code: {r.status_code}, ret message:{result['message']}")
        else:
            raise Exception(f"Connection failed")

    def query(self, param) -> pd.DataFrame:
        if self._access_token is None:
            raise Exception("Login required")
        r = self._query(param)
        if r.status_code == 200:
            # login succeed
            result = r.json()
            d = pd.DataFrame.from_records(result['data'], columns=param.get("fields"))
            return d
        elif r.status_code == 401:
            result = r.json()
            raise Exception(f"Login failed, return code: {r.status_code}, return message: {result['message']}")
        elif r.status_code == 400:
            result = r.json()
            raise Exception(f"Param errors, return code: {r.status_code}, return message: {result['message']}")
        else:
            raise Exception(f"Connection failed")

    def extract(self, param):
        d = self.query(param)
        return d



