"""
    Usage:
        magicli_example <name> [--amount=<int>]

        -a=<int> --amount=<int>  How often to greet
"""

from docopt import docopt
from magicli import magicli


def cli():
    magicli(docopt(__doc__))


def main(name, amount = 1):
    for _ in range(int(amount)):
        print(f'Hello {name}!')
