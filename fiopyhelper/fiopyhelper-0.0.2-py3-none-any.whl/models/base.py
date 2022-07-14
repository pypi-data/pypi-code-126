__all__ = ["BaseModel"]

class BaseModel:
    def __init__(self, **kwargs):
        self._id = kwargs.get("id")

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __bool__(self):
        return bool(self.id)

    def __str__(self):
        return self.id

    def is_not_none(self):
        return self._id is not None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def cleanup_values(self):
        for key, value in self.__dict__.items():
            if not isinstance(value, BaseModel) and value in ["JTNullValue", "null"]:
                self.__dict__[key] = None

