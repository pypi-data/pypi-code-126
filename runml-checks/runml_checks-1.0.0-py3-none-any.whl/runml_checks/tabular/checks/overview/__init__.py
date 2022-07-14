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
"""
Module contains check of overall overview of datasets and model.

.. deprecated:: 0.7.0
        `runml_checks.tabular.checks.overview is deprecated and will be removed in runml_checks 0.8 version.
        Use `runml_checks.tabular.checks.integrity` and :mod:`runml_checks.tabular.checks.model_evaluation` instead.
"""
import warnings

from ..data_integrity import ColumnsInfo
from ..model_evaluation import ModelInfo

__all__ = [
    'ModelInfo',
    'ColumnsInfo'
]

warnings.warn(
                'runml_checks.tabular.checks.overview is deprecated. Use runml_checks.tabular.checks.model_evaluation '
                'and runml_checks.tabular.checks.integrity instead.',
                DeprecationWarning
            )
