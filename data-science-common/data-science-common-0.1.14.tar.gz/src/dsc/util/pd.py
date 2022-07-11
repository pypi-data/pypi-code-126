# Standard library imports
from typing import Optional

# Third party imports
import pandas as pd
from tabulate import tabulate

# fmt: off
__all__ = [
    "tabulate_dataframe",
    "print_dataframe",
]
# fmt: on


def tabulate_dataframe(df: pd.DataFrame, nrows: Optional[int] = None) -> Optional[str]:
    """
    Creates a nicely formatted string/tables for a pandas dataframe

    Args:
        df (DataFrame):  the dataframe to print
        nrows (Optional[int]): the number of rows to display
    Returns:
        formatted dataframe sting-based output
    """

    if df.empty:
        print("pandas.DataFrame has no rows")
        return None
    return tabulate(df.head(nrows), headers="keys", tablefmt="psql")


def print_dataframe(df: pd.DataFrame, nrows: Optional[int] = None) -> None:
    """
    Prints a nicely formatted table for a pandas dataframe

    Args:
        df (DataFrame):  the dataframe to print
        nrows (Optional[int]): the number of rows to display
    """

    print(tabulate_dataframe(df, nrows=nrows))
