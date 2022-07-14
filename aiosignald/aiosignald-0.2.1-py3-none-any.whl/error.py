class SignaldException(Exception):
    """
    Base class to translate signald's response payloads into python exceptions
    """

    def __init__(self, payload: dict[str, str]):
        self.payload = payload
        for (k, v) in payload.items():
            setattr(self, k, v)
        self.type = self.__class__.__name__

    def __str__(self):
        return f"{self.__class__.__name__}: {self.payload}"


def raise_error(response: dict):
    """
    Raise a python exception using a signald response payload
    """
    if "error_type" in response:
        raise SignaldException(response["error_type"], response["error"])
