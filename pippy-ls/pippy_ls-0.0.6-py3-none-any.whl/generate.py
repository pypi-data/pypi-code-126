from random import randint
from colors import COLORS


def get_color():
    LIMIT = len(COLORS) - 1
    seed = randint(0, LIMIT)
    color = COLORS[seed]
    return color
