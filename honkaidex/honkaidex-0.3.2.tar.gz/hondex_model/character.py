from dataclasses import dataclass

from hondex_arch.baseDataclass import BaseDataclass


@dataclass(frozen=True)
class Character(BaseDataclass):
    weight: str
    height: str