#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.gcd import calculate_gcd


def main():
    start_game(calculate_gcd)


if __name__ == '__main__':
    main()
