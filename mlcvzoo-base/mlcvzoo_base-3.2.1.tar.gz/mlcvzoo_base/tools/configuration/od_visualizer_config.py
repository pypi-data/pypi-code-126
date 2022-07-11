# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for configuring the parsing of information from yaml in python
accessible attributes for the Object Detection (OD) Visualizer class
"""
import math
from typing import List

import related
from config_builder.BaseConfigClass import BaseConfigClass

from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.configuration.structs import FileNamePlaceholders
from mlcvzoo_base.configuration.visualization_config import VisualizationConfig


@related.mutable(strict=True)
class ODVisualizerInputDataImagesConfig(BaseConfigClass):
    """Class for parsing information of input image data"""

    file_extension: str = related.StringField(required=False, default=".jpg")
    input_dir: str = related.StringField(required=False, default="")
    sub_input_dirs: List[str] = related.SequenceField(str, required=False, default=[])
    start_frame: float = related.FloatField(required=False, default=0)
    stop_frame: float = related.FloatField(required=False, default=math.inf)


@related.mutable(strict=True)
class ODVisualizerInputDataVideoConfig(BaseConfigClass):
    """Class for parsing information of input video data"""

    input_path: str = related.StringField()
    start_frame: float = related.FloatField(required=False, default=0)
    stop_frame: float = related.FloatField(required=False, default=math.inf)
    skip_images: int = related.IntegerField(required=False, default=1)


@related.mutable(strict=True)
class ODVisualizerInputDataConfig(BaseConfigClass):
    """Class for parsing information of input data with reference to sub-parsers"""

    images: ODVisualizerInputDataImagesConfig = related.ChildField(
        ODVisualizerInputDataImagesConfig, required=False, default=None
    )

    video: ODVisualizerInputDataVideoConfig = related.ChildField(
        ODVisualizerInputDataVideoConfig, required=False, default=None
    )


@related.mutable(strict=True)
class ODVisualizerWriteOutputOutputConfig(BaseConfigClass):
    """Class for parsing information for image output saving procedure"""

    output_path: str = related.StringField()
    fps: int = related.IntegerField(required=False, default=1)
    output_shape: int = related.IntegerField(required=False, default=-1)


@related.mutable(strict=True)
class ODVisualizerWriteAnnotationConfig(BaseConfigClass):
    """Class for parsing information for annotation output saving procedure"""

    # Output directory for a predicted BaseAnnotation
    output_dir: str = related.StringField()
    # Filename of predicted BaseAnnotation.
    # Per default the placeholder IMAGE_NAME is replaced with
    # the input file-name.
    output_file_name: str = related.StringField(
        default=f"{FileNamePlaceholders.IMAGE_NAME}_predicted.xml"
    )


@related.mutable(strict=True)
class ODVisualizerWriteOutputConfig(BaseConfigClass):
    """Class for parsing information for output data with reference to sub-parsers"""

    ask_for_dir_creation = related.BooleanField(required=False, default=True)

    gif: ODVisualizerWriteOutputOutputConfig = related.ChildField(
        ODVisualizerWriteOutputOutputConfig, required=False, default=None
    )

    video: ODVisualizerWriteOutputOutputConfig = related.ChildField(
        ODVisualizerWriteOutputOutputConfig, required=False, default=None
    )

    annotation: ODVisualizerWriteAnnotationConfig = related.ChildField(
        ODVisualizerWriteAnnotationConfig, required=False, default=None
    )


@related.mutable(strict=True)
class ODVisualizerConfig(BaseConfigClass):
    """Class for parsing information from yaml in respective hierarchy"""

    input_data: ODVisualizerInputDataConfig = related.ChildField(
        cls=ODVisualizerInputDataConfig
    )

    model_configs: List[ModelConfig] = related.SequenceField(cls=ModelConfig)

    write_output: ODVisualizerWriteOutputConfig = related.ChildField(
        cls=ODVisualizerWriteOutputConfig,
        required=False,
        default=ODVisualizerWriteOutputConfig(),
    )

    visualization: VisualizationConfig = related.ChildField(
        cls=VisualizationConfig, default=VisualizationConfig()
    )
