import os
import typing as t


def assert_env_var(key: str, expected_value: t.Optional[str]) -> None:
    """Assert given environment variable has given value.

    Parameters
    ----------
    key : str
        Name of the variable.
    expected_value : str or None
        Expected value.

    Raises
    ------
    AssertionError
        If given environment variable does not have the expected value.

    """
    value = os.environ.get(key, None)
    assert value == expected_value
