"""Play the Game of Nim


Rules:
======

For the general description of the Nim and similar games, see the
`Wikipedia page`_.

This game is played by 2 palyers (the computer can be a player).
There are coins arranged in heaps.
There may be any number of heaps and any number of coins in a heap.

Players take turns. In each turn, a player takes coins from a heap (only 1
heap). It must be at least 1 coin. There is no upper limit (but the heap size).

There are 2 types of the game:

- the "normal" game is where the player, who takes the last coin, wins
- the "misère_" game is where the player, who has to take the last coin, loses


Usage:
======

After instantiating the Nim class, you need to get the heaps set up. The
starting heaps then can analysed and the starting player set. If it is the
Computer, it automatically does the 1st move. Then the Player is to do the next
move, then the Computer moves, and so on. When no more coins left, the game
ends.

Example::

    import nimgame
    nim = nimgame.Nim(error_rate=10)  # Request 10% error rate from the Computer
    nim.setup_heaps()  # Create heaps randomly
    nim.set_start(myturn=True)  # Indicate that the Player wants to start
    nim.do_move(nim.Move('b', 4))  # From heap 'B', remove 4 coins
    ...
    if nim.game_end():
        exit(0)


Available objects in the package
================================

While different objects are defined in the source on different level (e.g. the
Nim class in the source/core.py module), the necessary ones are made available
on package level, i.e. nimgame.Nim refers to that class.

:Nim: the main class of the game
:play_CLI: function that interactively plays the gam in CLI
:Move: namedtuple with "heapdesig" and "removecount" keys for defining a move.
    "heapdesig" can be an int (heap numbers start from zero), or a letter (case
    insensitive). E.g. 1 is the sames as "B" or "b".
:ErrorRate: namedtuple with "Computer" and "Player" keys for defining the
    required error rates in % for the players when both of them are simulated
:HeapCoinRange: namedtuple with "min" and "max" keys for defining heap number
    and sizes for automatic heap creation


Package content
===============

:source/core: provides the Nim class and its public methods
:source/calculations: mixin of the Nim class with calculation methods
:modules in "playing": functions to play the game
:modules in "tests": play several games automatically and gather statistics
:main: in the root directory provides some interactions for
    executing automatic runs or interactive games. This runs too, when the
    package is called (see the "__main__" module).


.. _Wikipedia page: https://en.wikipedia.org/wiki/Nim
.. _misère: https://en.wikipedia.org/wiki/Mis%C3%A8re#Mis%C3%A8re_game
"""
# Make sure the package base path is in the module import path (e.g. for flit)
import sys, os
basepath = os.path.dirname(__file__)
if basepath not in sys.path:
    sys.path.insert(0, basepath)

# Version info to be made available globally
from source import version
__version_info__ = version.__version_info__
__version__ = version.__version__

# Make the Nim class available on package level
from source.core import Nim
# Make structures available on package level
from source.typedefs import Move, ErrorRate, HeapCoinRange

# Make the playing functions available on package level
from source.playing.cli.play import play_CLI
from source.playing.web.play import playweb

# For the sake of linters, so that they do not complain of "unused" variables
__all__ = (
    Nim, 
    Move, ErrorRate, HeapCoinRange, 
    play_CLI, 
    playweb
)
