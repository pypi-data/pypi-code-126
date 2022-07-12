from enum import Enum

from pinyin_rhymer.error import NotAConsonantError


class Misc(Enum):
    NO_CONSONANT = ('',)

    def __new__(cls, spell):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        obj.spell = spell
        return obj

    def __str__(self):
        return self.spell


class ConsonantFamily(Enum):
    def __str__(self):
        return self.name

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
            return Misc.NO_CONSONANT
        try:
            return cls[name]
        except KeyError:
            # allowing each consonant to be written as a single alphabet
            translated = (
                name.replace('Z', 'zh').replace('C', 'ch').replace('S', 'sh')
            )
            for family in cls:
                if translated in family.__members__:
                    return family._member_map_[translated]
        raise NotAConsonantError(name)

    @classmethod
    def all(cls):
        all = {x for family in cls for x in family}
        all.add(Misc.NO_CONSONANT)
        return all

    @classmethod
    def all_as_str(cls):
        return {str(x) for x in cls.all()}
