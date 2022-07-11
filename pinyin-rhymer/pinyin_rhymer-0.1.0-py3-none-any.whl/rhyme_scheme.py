from enum import Enum, auto


class SchemeMethods(Enum):
    @classmethod
    def _missing_(cls, name):
        return cls(cls.__members__[name])


class ConsonantScheme(SchemeMethods):
    ALL = auto()
    FAMILY = auto()


class VowelScheme(SchemeMethods):
    TRADITIONAL = auto()
    SIMILAR_SOUNDING = auto()
    ADDTIIVE = auto()
    SUBTRACTIVE = auto()
