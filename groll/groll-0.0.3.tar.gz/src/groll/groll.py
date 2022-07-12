#!/usr/bin/env python3

import click
import importlib.metadata
import logging
import random
import re

from collections import deque

__version__ = importlib.metadata.version('groll')

DIE_STRING = r"^\d*d\d+$"
OP_STRING = r"^[\+-/\*]$"
NUM_STRING = r"^\d+$"
VALID_INPUT = r"|".join([DIE_STRING, OP_STRING, NUM_STRING])

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

logging.basicConfig(
    format="%(levelname)s : %(asctime)s : %(message)s",
    level=logging.DEBUG,
    filename="groll_error.log",
    filemode="w",
)


class InputLengthError(Exception):
    ...


class MissingOperand(Exception):
    ...


def print_usage_help() -> None:
    click.echo(" > type groll --help for more information")


def roll(obj: re.Match) -> str:
    num, sides = obj.group().split("d")
    if not num:
        num = 1
    else:
        num = int(num)
    sides = int(sides)
    total = 0
    for _ in range(num):
        total += random.randint(1, sides)
    return str(total)


def check_syntax(args: tuple) -> None:
    for _ in args:
        m = re.match(VALID_INPUT, _)
        if not m:
            click.secho(f" !!! {_} is not a recognised input!", fg="red")
            raise SyntaxError(_)
    logging.info("Syntax passed check")


def sub_rolls(argstr: str) -> str:
    logging.info(f"Rolling \"{argstr}\"...")
    argstr = re.sub(r"\d*d\d+", roll, argstr)
    return argstr


def eval_math_str(argstr: str) -> None:
    lhs = deque(argstr.split())
    if len(lhs) % 2 != 1:
        click.secho(" !!! Missing input...", fg="red")
        raise InputLengthError(lhs)
    x = int(lhs.popleft())
    logging.info(f"x = {x}")
    while lhs:
        op = lhs.popleft()
        try:
            y = lhs.popleft()
            y = int(y)
        except ValueError:
            click.secho(" !!! Missing operand...", fg="red")
            raise MissingOperand(y)
        logging.info(f"y = {y}, op = {op}")
        x = OPERATORS[op](x, y)
        logging.info(f"x = {x}")
    click.secho(f" > {x}", fg="bright_green")


def parse(args: tuple):
    try:
        check_syntax(args)
        argstr = " ".join(args)
        argstr = sub_rolls(argstr)
        eval_math_str(argstr)
    except Exception as e:
        print_usage_help()
        logging.critical(e, exc_info=True)


@click.command()
@click.option("-v", "--version", is_flag=True, help="display version")
@click.argument("dice", nargs=-1)
def cli(**kwargs):
    """A helpful, dice rolling, goblin that lives in your shell!"""
    logging.info("Started")
    logging.info(f"args captured from CL = {kwargs}")
    if kwargs["version"]:
        click.secho(f"groll v{importlib.metadata.version('groll')}", fg="bright_green")
    else:
        dice = kwargs["dice"]
        if not dice:
            dice = ("1d20",)
        parse(dice)
    logging.info("Finished")


if __name__ == "__main__":
    logging.info("Started")
    cli()
