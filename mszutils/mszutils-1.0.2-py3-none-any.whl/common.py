"""Provide functionality commonly used in various projects.

Example:
	>>> from mszutils.common import Text
	>>> Text.date_time_file_name()
	2022-07-08_09.07.34.334215

The module contains the following classes:

- `Text` - Performs operations on strings or returns strings for specific cases.
"""

import datetime

class Text:
    @staticmethod
    def date_time_file_name() -> str:
        """Returns date-time string which can be safely used as a file name.

        Example:
        	>>> Text.date_time_file_name()
	        2022-07-08_09.07.34.334215

        Returns:
        	A date-time string in format YYYY-MM-DD_HH.mm.ss.ffffff where `ffffff` denotes microseconds.
        """
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f")