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
Module contains checks for methodological flaws in the model building process.

.. deprecated:: 0.7.0
        `runml_checks.tabular.checks.methodology is deprecated and will be removed in runml_checks 0.8 version.
        Use `runml_checks.tabular.checks.model_evaluation`, `runml_checks.tabular.checks.train_test_validation`,
        `runml_checks.tabular.checks.integrity` instead.

"""
import warnings

from ..data_integrity import FeatureLabelCorrelation
from ..model_evaluation import BoostingOverfit, ModelInferenceTime, UnusedFeatures
from ..train_test_validation import (DatasetsSizeComparison, DateTrainTestLeakageDuplicates,
                                     DateTrainTestLeakageOverlap, FeatureLabelCorrelationChange,
                                     IdentifierLabelCorrelation, IndexTrainTestLeakage, TrainTestSamplesMix)

__all__ = [
    'BoostingOverfit',
    'UnusedFeatures',
    'FeatureLabelCorrelation',
    'FeatureLabelCorrelationChange',
    'IndexTrainTestLeakage',
    'TrainTestSamplesMix',
    'DateTrainTestLeakageDuplicates',
    'DateTrainTestLeakageOverlap',
    'IdentifierLabelCorrelation',
    'ModelInferenceTime',
    'DatasetsSizeComparison',
]


warnings.warn(
                'runml_checks.tabular.checks.methodology is deprecated and will be removed in runml_checks 0.8 version. '
                'Use runml_checks.tabular.checks.model_evaluation, runml_checks.tabular.checks.train_test_validation,'
                'runml_checks.tabular.checks.integrity` instead.',
                DeprecationWarning
            )
