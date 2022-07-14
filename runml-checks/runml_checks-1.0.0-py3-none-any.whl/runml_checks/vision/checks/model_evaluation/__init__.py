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
"""Module containing the model evaluation checks in the vision package."""
from .class_performance import ClassPerformance
from .confusion_matrix import ConfusionMatrixReport
from .image_segment_performance import ImageSegmentPerformance
from .mean_average_precision_report import MeanAveragePrecisionReport
from .mean_average_recall_report import MeanAverageRecallReport
from .model_error_analysis import ModelErrorAnalysis
from .robustness_report import RobustnessReport
from .simple_model_comparison import SimpleModelComparison
from .single_dataset_scalar_performance import SingleDatasetScalarPerformance
from .train_test_prediction_drift import TrainTestPredictionDrift

__all__ = [
    "TrainTestPredictionDrift",
    "ClassPerformance",
    "ConfusionMatrixReport",
    "ImageSegmentPerformance",
    "MeanAveragePrecisionReport",
    "MeanAverageRecallReport",
    "ModelErrorAnalysis",
    "RobustnessReport",
    "SimpleModelComparison",
    "SingleDatasetScalarPerformance",
]
