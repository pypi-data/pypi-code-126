from dataclasses import dataclass
import typing

from hondex_arch.baseDataclass import BaseDataclass
from hondex_model.character import Character


@dataclass(frozen=True)
class Battlesuit(BaseDataclass):
    character : Character
    version : str
    rank : str
    type : str
    core_strengths : str
    leader : str
    leaderEffect : str
    special : str
    specialEffect : str
    passive : str
    passiveEffect : str
    ultimate : str
    ultimateEffect : str
    evasion : str
    evasionEffect : str
    basic : str
    basicEffect : str
    core : str = None
    profile : str = None
    img : str = None

    def __post_init__(self):
        object.__setattr__(self, "character", Character.get(name=self.character.lower()))
        if self.core is not None:
            object.__setattr__(self, "core", Battlesuit.get(name=self.core.lower()))