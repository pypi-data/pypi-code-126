#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.even import calculate_even


def main():
    start_game(calculate_even)


if __name__ == '__main__':
    main()
