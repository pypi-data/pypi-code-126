import json


class Test(dict):
    """ Klasse zur Weiterleitung von Tests """

    @property
    def dauer(self) -> int:
        return self["Dauer"]

    def as_json_bytes(self) -> bytes:
        return json.dumps(self).encode("utf8")

    @classmethod
    def from_obj(cls, obj, /):
        if type(obj) in [bytes, str]:
            return cls(json.loads(obj))
        elif type(obj) == dict:
            return cls(obj)
    pass
