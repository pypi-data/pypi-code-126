from enum import Enum

__all__ = ["BaseEnum"]


class BaseEnum(Enum):
    def __str__(self):
        return str(self.value)
