#!/usr/bin/python3

import random
import argparse
import string

parser = argparse.ArgumentParser(description="Generate a random password")

parser.add_argument("-l",
                    "--length",
                    type=int,
                    default=8,
                    help="Length of password")

parser.add_argument("-n",
                    "--number",
                    type=int,
                    default=1,
                    help="Number of passwords to generate")

parser.add_argument("-o",
                    "--output",
                    metavar="PATH",
                    type=argparse.FileType("w", encoding="utf-8"),
                    default=None,
                    help="Path to output file")

parser.add_argument("-p",
                    "--punctuation",
                    default=False,
                    action="count",
                    help="Include pupnctuation. If another -p is given" +
                    "it will ONLY include punctuation.")

parser.add_argument("-d",
                    "--digit",
                    default=False,
                    action="count",
                    help="Include digits. If another -d is given," +
                    " it will ONLY include digits." +
                    " -dd takes precedence over -pp.")

parser.add_argument("-u",
                    "--upper",
                    default=False,
                    action="count",
                    help="Include uppercase letters. If another -u is given," +
                    " it will ONLY include uppercase letters." +
                    " -uu takes precedence over -pp and -dd.")

args = parser.parse_args()


def generate_password(length, number, output, upper, digit, punctuation):
    """
    Generate a random password
    """
    chars = string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if digit:
        chars += string.digits
    if punctuation:
        chars += string.punctuation

    if punctuation == 2:
        chars = string.punctuation
    if digit == 2:
        chars = string.digits
    if upper == 2:
        chars = string.ascii_uppercase

    passwords = [
        ''.join(random.choice(chars) for _ in range(length))
        for _ in range(number)
    ]

    if output:
        with open(output.name, "w") as f:
            for password in passwords:
                f.write(password + "\n")

    print("\n".join(passwords))


if __name__ == '__main__':

    generate_password(
        args.length,
        args.number,
        args.output,
        args.upper,
        args.digit,
        args.punctuation,
    )
