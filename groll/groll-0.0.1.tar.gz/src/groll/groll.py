#!/usr/bin/env python3

import click
import random
import re


DIE_PATTERN = r"\d*d\d+"
OPERATIONS = {
    "+": lambda a, b: str(a + b),
    "-": lambda a, b: str(a - b),
    "*": lambda a, b: str(a * b),
    "/": lambda a, b: str(a // b),
}


def roll(pattern, args):
    results = []
    for arg in args:
        if re.match(DIE_PATTERN, arg):
            num, sides = arg.split("d")
            if not num:
                num = 1
            num = int(num)
            sides = int(sides)
            arg = num * random.randint(1, sides)
        results.append(str(arg))
    return results


def eval_maths(result):
    return str(OPERATIONS[result[1]](int(result[0]), int(result[2])))


def parse(args, verbose):
    result = roll(DIE_PATTERN, args)
    if verbose:
        click.echo(f" -> {' '.join(result)}")
    while len(result) > 1:
        tmp = [eval_maths(result)]
        tmp.extend(result[3:])
        result = tmp[:]
    click.echo(click.style(f" -> {int(result[0])}", fg="bright_green"))


@click.command()
@click.option("-v", "--verbose", is_flag=True)
@click.argument("args", nargs=-1)
def cli(args: tuple[str], verbose: bool) -> None:
    if not args:
        args = ("1d20",)
    if verbose:
        click.echo(f" -> rolling {' '.join(args)}")
    parse(args, verbose)


if __name__ == "__main__":
    cli()
