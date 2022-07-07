#!/usr/bin/env python3
import sys
import argparse
import json


def print_atom_json(val):
    print(json.dumps(val))


def print_iterable(val):
    for x in val:
        args.print_atom(x)


def handle_value_grep(value, line):
    if value:
        args.print_value(line)


def handle_value_normal(value, line):
    args.print_value(value)


def handle_value_truish(value, line):
    if value:
        args.print_value(value)


def handle_value_none(value, line):
    if value is not None:
        args.print_value(value)


parser = argparse.ArgumentParser(
    description="Shortcut for using Python for line processing",
)

parser.set_defaults(
    handle_value=handle_value_normal,
    print_value=print,
    print_atom=print,
)

shape = parser.add_mutually_exclusive_group()
shape.add_argument(
    "-l",
    "--lines",
    action="store_true",
    help="Evaluate expression once, with the `lines` generator instead of `i`",
)
shape.add_argument(
    "-g",
    "--grep",
    action="store_const",
    const=handle_value_grep,
    dest="handle_value",
    help="Instead of printing the value use it for filtering lines",
)
shape.add_argument(
    "-t",
    "--truish",
    action="store_const",
    const=handle_value_truish,
    dest="handle_value",
    help="Print only values where bool(val) == True",
)
shape.add_argument(
    "-n",
    "--none",
    action="store_const",
    const=handle_value_none,
    dest="handle_value",
    help="Print only values where val != None",
)

parser.add_argument(
    "-i",
    "--iterable",
    action="store_const",
    const=print_iterable,
    dest="print_value",
    help="Threat resulting value as iterable of separate lines. Usefull with --lines, ignored with --grep",
)

parser.add_argument(
    "-j",
    "--json",
    action="store_const",
    const=print_atom_json,
    dest="print_atom",
    help="Print value using json.dump(). Together with --iterable results in NDJSON, ignored with --grep",
)

parser.add_argument("expr", metavar="E", help="expression to evaluate")

def main():
    global args
    args = parser.parse_args()
    expr = args.expr

    if args.lines:
        lines = map(lambda x: x.rstrip("\n"), sys.stdin)
        lcls = dict(lines=lines)
        value = eval(expr, None, lcls)
        args.print_value(value)
    else:
        for line in sys.stdin:
            line = line.rstrip("\n")
            lcls = dict(i=line)
            value = eval(expr, None, lcls)
            args.handle_value(value, line)

if __name__ == '__main__':
    main()
