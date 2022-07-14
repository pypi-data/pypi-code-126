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
"""Alternative way to import tabular suites.

This module exists only for backward compatibility and will be
removed in the nexts versions.
"""
# flake8: noqa
import warnings

from runml_checks.tabular.suites import *  # pylint: disable=wildcard-import

warnings.warn(
    'Ability to import tabular suites from the `runml_checks.suites` '
    'is deprecated, please import from `runml_checks.tabular.suites` instead',
    DeprecationWarning
)


__all__ = [
    'single_dataset_integrity',
    'train_test_leakage',
    'train_test_validation',
    'model_evaluation',
    'full_suite',
    'data_integrity',
]
