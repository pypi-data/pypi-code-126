from enum import Enum


class ConsonantFamily(object):
    def family(self):
        cls = self.__class__
        return cls._member_map_


class Consonant(Enum):
    Plosive = ('Plosive', 'b d g p t k')
    Affricate = ('Affricate', 'z zh j c ch q')
    Fricative = ('Fricative', 'f x s sh h')
    Lateral = ('Lateral', 'l r')
    Nasal = ('Nasal', 'm n')

    def __new__(cls, name, value, *args):
        return Enum(name, value, type=ConsonantFamily)

    @classmethod
    def get(cls, name):
        if not name:
            return None
        try:
            return cls[name]
        except KeyError:
            for family in cls:
                if name in family.__members__:
                    return family._member_map_[name]
        raise KeyError

    @classmethod
    def all(cls):
        all = {x.name for family in cls for x in family}
        all.add('')
        return all
