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
"""Type definitions."""
from typing import List

# pylint: disable=invalid-hash-returned,invalid-name
from typing_extensions import Protocol, runtime_checkable

__all__ = ['Hashable', 'BasicModel', 'ClassificationModel']


@runtime_checkable
class Hashable(Protocol):
    """Trait for any hashable type that also defines comparison operators."""

    def __hash__(self) -> int:  # noqa: D105
        ...

    def __le__(self, __value) -> bool:  # noqa: D105
        ...

    def __lt__(self, __value) -> bool:  # noqa: D105
        ...

    def __ge__(self, __value) -> bool:  # noqa: D105
        ...

    def __gt__(self, __value) -> bool:  # noqa: D105
        ...

    def __eq__(self, __value) -> bool:  # noqa: D105
        ...


@runtime_checkable
class BasicModel(Protocol):
    """Traits of a model that are necessary for runml_checks."""

    def predict(self, X) -> List[Hashable]:
        """Predict on given X."""


@runtime_checkable
class ClassificationModel(BasicModel, Protocol):
    """Traits of a classification model that are used by runml_checks."""

    def predict_proba(self, X) -> List[Hashable]:
        """Predict probabilities on given X."""
