from dataclasses import dataclass
import typing

from hondex_arch.baseDataclass import BaseDataclass
import dataclasses

@dataclass(frozen=True)
class StigmataSet(BaseDataclass):
    obtain : typing.List[str]
    rarity : str = None
    version : str = None
    slotT_effect : str = None
    slotM_effect : str = None
    slotB_effect : str = None
    setEffect2p : str = None
    setEffect3p : str = None
    img_t : str = None
    img_m : str = None
    img_b : str = None
    icon_m : str = None
    icon_b : str = None
    icon_t : str = None

