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
"""Objects validation utilities."""

# TODO: move tabular functionality to the tabular sub-package

import typing as t

from runml_checks.core import errors
from runml_checks.utils.typing import Hashable

__all__ = [
    'ensure_hashable_or_mutable_sequence',
]


T = t.TypeVar('T', bound=Hashable)


def ensure_hashable_or_mutable_sequence(
    value: t.Union[T, t.MutableSequence[T]],
    message: str = (
        'Provided value is neither hashable nor mutable '
        'sequence of hashable items. Got {type}')
) -> t.List[T]:
    """Validate that provided value is either hashable or mutable sequence of hashable values."""
    if isinstance(value, Hashable):
        return [value]

    if isinstance(value, t.MutableSequence):
        if len(value) > 0 and not isinstance(value[0], Hashable):
            raise errors.runml_checksValueError(message.format(
                type=f'MutableSequence[{type(value).__name__}]'
            ))
        return list(value)

    raise errors.runml_checksValueError(message.format(
        type=type(value).__name__
    ))
