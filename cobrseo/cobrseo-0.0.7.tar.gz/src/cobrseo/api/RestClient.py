from http.client import HTTPSConnection
import json


class RestClient:
    domain = 'api.dataforseo.com'

    def __init__(self, credential):
        self.credential = credential

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)

        try:
            headers = {
                'Authorization': f'Basic {self.credential}',
                'Content-Type': 'application/json'
            }
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()

            return json.loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = json.dumps(data)
        return self.request(path, 'POST', data_str)
