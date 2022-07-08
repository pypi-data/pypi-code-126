#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Package for using dates stored as int

    ASSUMPTIONS:
        The tools module assumes dates are valid and are of the expected type.
        Use the Undated class or convert with as_int if unsure values are valid.

    LIMITATIONS:
        Uses the Gregorian calendar and makes no adjustment for the Julian calendar changeover.
        Therefore only use dates from 1583 onwards.
"""
# -----------------------------------------------

from ._tools import *

# -----------------------------------------------
# End.
