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
"""Package for vision functionality."""
from .base_checks import ModelOnlyCheck, SingleDatasetCheck, TrainTestCheck
from .batch_wrapper import Batch
from .classification_data import ClassificationData
from .context import Context
from .detection_data import DetectionData
from .simple_classification_data import SimpleClassificationData, SimpleClassificationDataset
from .suite import Suite
from .vision_data import VisionData

try:
    import torch  # noqa: F401
    import torchvision  # noqa: F401
except ImportError as error:
    raise ImportError("PyTorch is not installed. Please install torch and torchvision "
                      "in order to use runml_checks.vision functionalities.") from error


__all__ = [
    "VisionData",
    "ClassificationData",
    "DetectionData",
    "SimpleClassificationDataset",
    "SimpleClassificationData",
    "Context",
    "SingleDatasetCheck",
    "TrainTestCheck",
    "ModelOnlyCheck",
    "Suite",
    "Batch"
]
