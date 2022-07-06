import re
from typing import List


def class_case_to_snake_case(string: str) -> str:
    """
    >>> class_case_to_snake_case('SomeString')
    'some_string' """

    return '_'.join(
            map(
                lambda token: token.lower(),
                split_at_uppercase(string)
            )
        )


def split_at_uppercase(string: str) -> List[str]:
    """
    >>> split_at_uppercase("EisgekuehlterBomelunder")
    ['Eisgekuehlter', 'Bomelunder'] """

    return re.findall('[A-Z][a-z]*', string)