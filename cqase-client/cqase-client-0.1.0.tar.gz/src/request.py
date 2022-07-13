import requests

from src.models import ResponseModel


class Response:
    @staticmethod
    def structure_response(response) -> ResponseModel:
        return ResponseModel(response.status_code, response.json())


class Client:
    def __init__(self, headers: dict):
        self.headers = headers

    s = requests.session()

    def request(self, method: str, url: str, **kwargs) -> ResponseModel:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return Response.structure_response(
            self.s.request(method, url, headers=self.headers, **kwargs)
        )
