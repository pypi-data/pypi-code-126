from collections import namedtuple

Dice = namedtuple('Dice', ['face'])

"""Main module."""


class Dicy:

    def __init__(self):
        self._dice = [Dice(face) for face in range(1, 7)]

    def __len__(self):
        return len(self._dice)

    def __getitem__(self, position):
        return self._dice[position]
