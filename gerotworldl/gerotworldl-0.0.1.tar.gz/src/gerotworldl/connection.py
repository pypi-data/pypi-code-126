import json.decoder

import requests
import urllib3.exceptions


class Connection:
    def __init__(self, url):
        self.url = url
        self.connection = None
        self.serverData = None
        self.mainurl = None

    def connect(self):
        try:
            requests.get(self.mainurl)
            self.connection = requests.get(self.url)
        except requests.exceptions.ConnectionError and urllib3.exceptions.MaxRetryError:
            return False
        try:
            self.serverData = self.connection.json()
        except requests.exceptions.JSONDecodeError and json.decoder.JSONDecodeError:
            return False
        if not self.serverData['connectAccept']:
            return False
        return True

    def getauthuser(self, query, mysql):
        user = mysql.query(query)
        if not user:
            return None
        return user

    def setmainurl(self, url):
        self.mainurl = url

    def getmainurl(self):
        return self.mainurl

    def getserverdata(self):
        return self.serverData


