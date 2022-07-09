from enum import Enum
from typing import List


class AutoName(Enum):
    def _generate_next_value_(name, *args):
        # https://docs.python.org/3/library/enum.html#using-automatic-values
        return name.lower()

    @classmethod
    def to_list(cls) -> List[str]:
        """Get all values, put them into a list and return.

        Returns
        -------
        List[str]
        """
        return [attr.value for attr in cls]


class NSFWImageTags(AutoName):
    LEWD = "lewd"
    GASM = "gasm"
    SPANK = "spank"


class SFWImageTags(AutoName):
    WALLPAPER = "wallpaper"
    NGIF = "ngif"
    TICKLE = "tickle"
    FEED = "feed"
    GECG = "gecg"
    SLAP = "slap"
    AVATAR = "avatar"
    WAIFU = "waifu"
    PAT = "pat"
    KISS = "kiss"
    NEKO = "neko"
    CUDDLE = "cuddle"
    FOX_GIRL = "fox_girl"
    HUG = "hug"
    SMUG = "smug"


class RealSFWImageTags(AutoName):
    LIZARD = "lizard"
    EIGHT_BALL = "8ball"
    GOOSE = "goose"
    WOOF = "woof"
