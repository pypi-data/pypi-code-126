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
"""Module containing the performance check in the vision package.

.. deprecated:: 0.7.0
        `runml_checks.vision.checks.performance is deprecated and will be removed in runml_checks 0.8 version.
        Use `runml_checks.vision.checks.model_evaluation` instead.
"""
import warnings

from ..model_evaluation import (ClassPerformance, ConfusionMatrixReport, ImageSegmentPerformance,
                                MeanAveragePrecisionReport, MeanAverageRecallReport, ModelErrorAnalysis,
                                RobustnessReport, SimpleModelComparison)

__all__ = [
    "ClassPerformance",
    "MeanAveragePrecisionReport",
    "MeanAverageRecallReport",
    "RobustnessReport",
    "SimpleModelComparison",
    "ConfusionMatrixReport",
    "ModelErrorAnalysis",
    "ImageSegmentPerformance",
]

warnings.warn(
    "runml_checks.vision.checks.performance is deprecated. Use runml_checks.vision.checks.model_evaluation instead.",
    DeprecationWarning
)
