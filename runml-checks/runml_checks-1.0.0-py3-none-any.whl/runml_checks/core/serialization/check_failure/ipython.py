# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 runml_checks (https://www.runml_checks.com)
#
# This file is part of runml_checks.
# runml_checks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with runml_checks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
#
"""Module containing CheckFailuer serialization logic."""
import typing as t

from IPython.display import HTML

from runml_checks.core import check_result as check_types
from runml_checks.core.serialization.abc import IPythonFormatter, IPythonSerializer

from . import html

__all__ = ['CheckFailureSerializer']


class CheckFailureSerializer(IPythonSerializer['check_types.CheckFailure']):
    """Serializes any CheckFailure instance into a list of IPython formatters.

    Parameters
    ----------
    value : CheckFailure
        CheckFailure instance that needed to be serialized.
    """

    def __init__(self, value: 'check_types.CheckFailure', **kwargs):
        if not isinstance(value, check_types.CheckFailure):
            raise TypeError(
                f'Expected "CheckFailure" but got "{type(value).__name__}"'
            )
        super().__init__(value=value)
        self._html_serializer = html.CheckFailureSerializer(value)

    def serialize(self, **kwargs) -> t.List[IPythonFormatter]:
        """Serialize a CheckFailure instance into a list of IPython formatters.

        Returns
        -------
        List[IPythonFormatter]
        """
        return [HTML(self._html_serializer.serialize())]
