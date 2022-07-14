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
"""Module containing the distribution checks in the vision package.

.. deprecated:: 0.7.0
        `runml_checks.vision.checks.distribution is deprecated and will be removed in runml_checks 0.8 version.
        Use `runml_checks.vision.checks.train_test_validation`, `runml_checks.vision.checks.data_integrity`
        and `runml_checks.vision.checks.model_evaluation` instead.
"""
import warnings

from ..data_integrity import ImagePropertyOutliers, LabelPropertyOutliers
from ..model_evaluation import TrainTestPredictionDrift
from ..train_test_validation import (HeatmapComparison, ImageDatasetDrift, ImagePropertyDrift, NewLabels,
                                     TrainTestLabelDrift)

__all__ = [
    'TrainTestLabelDrift',
    'TrainTestPredictionDrift',
    'ImageDatasetDrift',
    'HeatmapComparison',
    'ImagePropertyDrift',
    'ImagePropertyOutliers',
    'LabelPropertyOutliers',
    'NewLabels'
]

warnings.warn(
                'runml_checks.vision.checks.distribution is deprecated. Use '
                'runml_checks.vision.checks.train_test_validation, runml_checks.vision.checks.data_integrity'
                'and runml_checks.vision.checks.model_evaluation instead.',
                DeprecationWarning
            )
