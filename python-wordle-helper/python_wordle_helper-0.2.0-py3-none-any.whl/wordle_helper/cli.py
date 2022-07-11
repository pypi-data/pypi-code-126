from argparse import ArgumentParser
import logging
import os
import random
import sys
from uuid import uuid4
from typing import List

import numpy as np
import requests
from wordfreq import zipf_frequency


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
WORDS_URL = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"


def filter_n_occurrences(letter: str, bounds: List[int], words: np.array) -> np.array:
    """
    Filters out words with fewer than `min` or greater than `max` occurrences of `letter`

    :param letter: The letter to filter out
    :type letter: str
    :param bounds: The minimum and maximum number of times the letter should occur
    :type min_: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)
    _max = max(bounds)
    _min = min(bounds)
    mask = [_max >= (word == ordinal).sum() >= _min for word in words]
    return words[mask]


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


def filter_multiple_locations(
    letter: str, locations: int, count: List[int], words: np.array
) -> np.array:
    """
    Removes words without the letter `letter` and words with `letter` in at least one of the
    locations in `locations`

    :param letter: The letter to consider
    :type letter: str
    :param locations: The locations that the letter cannot be in
    :type locations: int
    :param count: The minimum and maximum number of times the letter must occur in the word
    :type count: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)

    # Remove words containing `letter` at each given location
    for location in locations:
        words = words[words[:, location - 1] != ordinal, :]

    # Remove words not containing the desired occurrences of `letter`
    return filter_n_occurrences(letter, count, words)


def filter_single_location(
    letter: str, locations: List[int], count: List[int], words: np.array
) -> np.array:
    """
    Removes words without `letter` at `locations'.

    :param letter: The letter that must exist at `locations`
    :type letter: str
    :param locations: The locations that `letter` must be
    :type locations: List[int]
    :param count: The minimum and maximum number of times the letter must occur in the word
    :type count: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """

    for location in locations:
        # Remove words without `letter` at `location`
        words = words[words[:, location - 1] == ord(letter), :]

    # Remove words not containing the desired occurrences of `letter`
    return filter_n_occurrences(letter, count, words)


def constraints_to_dict(constraints: List[str]) -> dict:
    """
    Parses the list of constraints into a dictionary. Each element of the list takes the form of
    <letter><operation><locations>, where <letter> is the letter that this constraint applies to,
    <operation> is the type of constraint, and <locations> is the list of locations in the string to
    apply the constraint. The valid values for <operation> are:

    "y": represents yellow letters. For example, if your guess has a yellow letter "e" in the second
    position, you would type "ey2". And if your next guess had a yellow "e" in the fifth position,
    you would update that to "ey25".

    "b": represents unused letters. For example, if your guess has unused letter "w" (in any
    position) you would type "wb". This operation takes zero locations, because it does not appear
    anywhere.

    "g": represents green letters. For example, if your guess has a green letter "e" in the third
    position, you would type "eg3".

    "c": represents the count, i.e. minimum and maximum number of occurrences of the letter in the
    word. For example, if you have a green letter "a" in one spot and a yellow "a" in another (for
    the same guess), you know there must be at least two a's in the word and you would type "ac25".

    :param constraints: The list of constraints to interpret
    :type constraints: list[str]
    :rtype: dict
    """
    constraint_dict = {}
    for letter_constraint in constraints:
        letter, operation, *positions = letter_constraint
        if letter not in constraint_dict:
            constraint_dict[letter] = {}

        letter_dict = constraint_dict[letter]
        if operation in letter_dict:
            if operation in ["b", "c"]:
                raise ValueError(f"Operation {operation} can only be specified once")
        else:
            if operation in ["b", "c", "g", "y"]:
                letter_dict[operation] = []
            else:
                raise ValueError(
                    f"Found invalid operation '{operation}', expecting one of 'b', 'c', 'g', or 'y'"
                )

        if operation == "b":
            # Takes no position
            continue

        letter_dict[operation].extend(int(pos) for pos in positions)

    return constraint_dict


def find_remaining_words(word_list: List[str], constraints: dict) -> List[str]:
    """
    Finds the words that are valid once all constraints are considered. Returns the list of valid
    words sorted by frequency of use in the English language.

    :param word_list:
    :type word_list: list[str]
    :param constraints:
    :type constraints: dict
    :rtype: list[str]
    """
    default_bounds = [1, 5]
    word_arr = np.array([[ch for ch in wd] for wd in word_list])
    for letter, letter_constraints in constraints.items():
        bounds = letter_constraints.get("c", default_bounds)
        for op, locations in letter_constraints.items():
            if op == "c":
                # Skip this operation, it is only used in conjunction with "y" and "g"
                continue
            elif op == "b":
                word_arr = filter_out_letter(letter, word_arr)
            elif op == "y":
                word_arr = filter_multiple_locations(letter, locations, bounds, word_arr)
            elif op == "g":
                word_arr = filter_single_location(letter, locations, bounds, word_arr)
            else:
                LOGGER.warning(f"Invalid operation '{op}', skipping constraint on '{letter}'")

    word_lst = ["".join(chr(ch) for ch in word) for word in word_arr]
    word_lst.sort(key=lambda wrd: zipf_frequency(wrd, "en"), reverse=True)
    return word_lst


def get_word_list_from_url(list_url: str = WORDS_URL) -> List[str]:
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
        LOGGER.info(f"Found {len(word_list)} possibilites, the most common one is '{word_list[0]}'")
        if len(word_list) < cutoff_len:
            all_guesses = "\n".join(word_list)
            LOGGER.info(f"All valid guesses, sorted by frequency:\n{all_guesses}")
        else:
            fn = f"words_{uuid4().hex}"
            with open(fn, "w") as fp:
                for word in word_list:
                    fp.writelines(f"{word}\n")
            LOGGER.info(f"Check {fn} for all possibilites, sorted by frequency")
    else:
        LOGGER.warning("No choices found!")


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
