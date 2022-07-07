from argparse import ArgumentParser
import os
import random
import sys
from uuid import uuid4

import numpy as np
import requests
from wordfreq import zipf_frequency


WORDS_URL = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"


def filter_out_letter(letter: str, words: np.array) -> np.array:
    """
    Removes all words containing the letter `letter`

    :param letter: The letter to filter out
    :type letter: str
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)
    mask = [ordinal not in word for word in words]
    return words[mask]


def filter_multiple_locations(letter: str, locations: int, words: np.array) -> np.array:
    """
    Removes words without the letter `letter` and words with `letter` in at least one of the
    locations in `locations`

    :param letter: The letter to consider
    :type letter: str
    :param locations: The locations that the letter cannot be in
    :type locations: int
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)

    # Remove words containing `letter` at each given location
    for location in locations:
        words = words[words[:, location] != ordinal, :]

    # Remove words not containing `letter` at all
    mask = [ordinal in word for word in words]
    return words[mask]


def filter_single_location(letter: str, location: int, words: np.array) -> np.array:
    """
    Removes words without `letter` at `location'.

    :param letter: The letter that cannot exist at `location`
    :type letter: str
    :param location: The location that `letter` cannot exist
    :type location: int
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    return words[words[:, location] == ord(letter), :]


def constraints_to_dict(constraints: list[str]) -> dict:
    """
    Parses the list of constraints into a dictionary. Each element of the list takes the form of
    <letter><operation><locations>, where <letter> is the letter that this constraint applies to,
    <operation> is the type of constraint, and <locations> is the list of locations in the string to
    apply the constraint. The valid values for <operation> are:

    "y": represents yellow letters. For example, if your guess has a yellow letter "e" in the second
    position, you would type "ey1". And if your next guess had a yellow "e" in the fifth position,
    you would update that to "ey14". 

    "b": represents unused letters. For example, if your guess has unused letter "w" (in any
    position) you would type "wb". This operation takes zero locations, because it does not appear
    anywhere.

    "g": represents green letters. For example, if your guess has a green letter "e" in the third
    position, you would type "eg2".

    :param constraints: The list of constraints to interpret
    :type constraints: list[str]
    :rtype: dict
    """
    constraint_dict = {}
    for letter_constraint in constraints:
        letter, operation, *positions = letter_constraint
        constraint_dict[letter] = {
            "locations": [int(pos) for pos in positions],
            "operation": operation,
        }
    return constraint_dict


def find_remaining_words(word_list: list[str], constraints: dict) -> list[str]:
    """
    Finds the words that are valid once all constraints are considered. Returns the list of valid
    words sorted by frequency of use in the English language.

    :param word_list:
    :type word_list: list[str]
    :param constraints:
    :type constraints: dict
    :rtype: list[str]
    """
    word_arr = np.array([[ch for ch in wd] for wd in word_list])
    for letter, constraints in constraints.items():
        op = constraints["operation"]
        locations = constraints["locations"]
        if op == "b":
            word_arr = filter_out_letter(letter, word_arr)
        elif op == "y":
            word_arr = filter_multiple_locations(letter, locations, word_arr)
        elif op == "g":
            word_arr = filter_single_location(letter, locations[0], word_arr)
        else:
            print(f"Invalid operation '{op}', skipping constraint on '{letter}'")

    word_lst = ["".join(chr(ch) for ch in word) for word in word_arr]
    word_lst.sort(key=lambda wrd: zipf_frequency(wrd, "en"), reverse=True)
    return word_lst


def get_word_list_from_url(list_url: str = WORDS_URL) -> list[str]:
    """
    Returns a list of 5 letter words

    :param list_url: The URL from which to get the words list. The content in the response is
                     expected to be a newline-delimited string of words.
    :type list_url: str
    :rtype: list[str]
    """
    r = requests.get(WORDS_URL, allow_redirects=True)
    return r.content.split(b"\n")


def print_or_save_word_list(word_list: str, cutoff_len: int = 42) -> None:
    """
    Prints or saves the remaining word list, depending on its length

    :param word_list: The list of words to print or save to a file
    :type word_list: str
    :param cutoff_len: If `word_list` is `cutoff_len` or longer, the list is saved to a file
    :type cutoff_len: int
    :rtype: None
    """
    """"""
    if word_list:
        print(f"Found {len(word_list)} possibilites, the most common one is '{word_list[0]}'")
        if len(word_list) < cutoff_len:
            all_guesses = "\n".join(word_list)
            print(f"All valid guesses, sorted by frequency:\n{all_guesses}")
        else:
            fn = f"words_{uuid4().hex}"
            with open(fn, "w") as fp:
                for word in word_list:
                    fp.writelines(f"{word}\n")
            print(f"Check {fn} for all possibilites, sorted by frequency")
    else:
        print("No choices found!")


def main():
    parser = ArgumentParser(description="Cheat at wordle!")
    parser.add_argument("letters", type=str, nargs="+")
    args = parser.parse_args()

    constraint_dict = constraints_to_dict(args.letters)
    word_list = get_word_list_from_url()
    remaining_words = find_remaining_words(word_list, constraint_dict)
    print_or_save_word_list(remaining_words)


if __name__ == "__main__":
    main()
