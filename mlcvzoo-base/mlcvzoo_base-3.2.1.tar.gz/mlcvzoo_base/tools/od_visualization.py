# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for object detection visualization"""
import logging
import os
import typing
from typing import Any, Dict, List, Optional

import cv2
import numpy as np
from config_builder.ConfigBuilder import ConfigBuilder
from tqdm import tqdm

from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.data.bounding_box import BoundingBox
from mlcvzoo_base.api.model import (
    ConfigurationType,
    DataType,
    Model,
    ObjectDetectionModel,
    PredictionType,
)
from mlcvzoo_base.configuration.structs import FileNamePlaceholders
from mlcvzoo_base.data_preparation.utils import annotation_to_xml
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils.draw_utils import (
    draw_on_image,
    draw_on_pil_image,
    generate_detector_colors,
)
from mlcvzoo_base.utils.file_utils import get_file_list, get_project_path_information
from mlcvzoo_base.utils.image_io_utils import (
    GifFileOutput,
    VideoFileInput,
    VideoFileOutput,
    VideoLiveOutput,
)

from .configuration.od_visualizer_config import ODVisualizerConfig

logger = logging.getLogger("{}".format(__name__))


class ObjectDetectionVisualizer(ConfigBuilder):
    """
    Tool to visualize the detection results of a model, save the results as video or gif and generate xml annotations
    from the detection results
    """

    gt_annotations: List[BaseAnnotation]

    # INPUT:
    file_paths: Optional[List[str]] = None
    video_file_input: Optional[VideoFileInput] = None

    # OUTPUT
    video_live_output: Optional[VideoLiveOutput] = None
    gif_file_output: Optional[GifFileOutput] = None
    video_file_output: Optional[VideoFileOutput] = None

    def __init__(
        self,
        yaml_config_path: Optional[str] = None,
        configuration: Optional[ODVisualizerConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
    ) -> None:

        ConfigBuilder.__init__(
            self,
            class_type=ODVisualizerConfig,
            configuration=configuration,
            yaml_config_path=yaml_config_path,
            argparse_module_description="Tool for running Object-Detection "
            "model inference and generating \n"
            "helpful output files like gifs, videos, annotations.",
            mutual_attribute_map=mutual_attribute_map,
            no_checks=no_checks,
            string_replacement_map=string_replacement_map,
        )

        self.config = typing.cast(ODVisualizerConfig, self.configuration)

        self.model_registry = ModelRegistry()

        self.__init_input_data()

        self.__init_image_io()

        logger.debug("Object detection visualization initialized")

    def __init_input_data(self) -> None:

        """
        Inits input files and input videos specified in config yaml
        """

        if self.config.input_data.images is not None and self.file_paths is None:

            self.file_paths = []
            if len(self.config.input_data.images.sub_input_dirs) > 0:

                for sub_input_dir in self.config.input_data.images.sub_input_dirs:
                    self.file_paths.extend(
                        get_file_list(
                            input_dir=os.path.join(
                                self.config.input_data.images.input_dir, sub_input_dir
                            ),
                            search_subfolders=True,
                            file_extension=self.config.input_data.images.file_extension,
                        )
                    )
            else:
                self.file_paths.extend(
                    get_file_list(
                        input_dir=self.config.input_data.images.input_dir,
                        search_subfolders=True,
                        file_extension=self.config.input_data.images.file_extension,
                    )
                )

        if self.config.input_data.video is not None:
            if self.video_file_input is None:
                self.video_file_input = VideoFileInput(
                    path=self.config.input_data.video.input_path
                )
            else:
                # Reset video for next run
                self.video_file_input.goto_frame(0)

    def __init_image_io(self) -> None:

        """
        Inits object for every output type specified in config yaml:
            - Object for creating gif output file
            - Object for creating video output file
            - Object for stepping frame by frame through video and displaying annotations
        """

        if self.gif_file_output is not None:
            del self.gif_file_output

        if self.config.write_output.gif is not None:
            self.gif_file_output = GifFileOutput(
                output_path=self.config.write_output.gif.output_path,
                fps=self.config.write_output.gif.fps,
                output_shape=self.config.write_output.gif.output_shape,
                ask_for_dir_creation=self.config.write_output.ask_for_dir_creation,
            )

        if self.video_file_output is not None:
            del self.video_file_output

        if self.config.write_output.video is not None:
            self.video_file_output = VideoFileOutput(
                path=self.config.write_output.video.output_path,
                fps=self.config.write_output.video.fps,
                output_shape=self.config.write_output.video.output_shape,
            )

        if self.video_live_output is not None:
            del self.video_live_output

        if self.config.visualization.show_image:
            self.video_live_output = VideoLiveOutput(
                window_size=self.config.visualization.output_shape, show_fps=True
            )

    def __add_frame_to_image_io(self, frame: np.ndarray) -> None:  # type: ignore[type-arg]

        """
        Adds frame to associated output object
        Args:
            frame: N-dimensional Array representing single frame
        """

        if self.gif_file_output is not None:
            self.gif_file_output.add_frame(frame=frame)

        if self.video_file_output is not None:
            self.video_file_output.add_frame(frame=frame)

        if self.video_live_output is not None:
            self.video_live_output.output_frame(frame=frame)

    def __write_image_io(self) -> None:

        """
        Saves generated output gif and output video
        """

        if self.gif_file_output is not None:
            self.gif_file_output.save_gif()

        if self.video_file_output is not None:
            self.video_file_output.close()

    def __visualization_step(
        self,
        frame: np.ndarray,  # type: ignore[type-arg]
        bounding_boxes: List[BoundingBox],
        rgb_colors: Any,
    ) -> None:

        """
        Draws given bounding boxes on input frame and adds the resulting frame to its associated output object
        Args:
            frame: N-dimensional Array representing single frame
            bounding_boxes: List of bounding box objects
            rgb_colors: List[Tuples(int, int, int)] specifying bounding box color with len(List) == number of classes
        """

        if os.path.isfile(self.config.visualization.font_path):
            annotated_frame = draw_on_pil_image(
                image=frame,
                bounding_boxes=bounding_boxes,
                font_path=self.config.visualization.font_path,
                rgb_colors=rgb_colors,
                thickness=2,
            )
        else:
            annotated_frame = draw_on_image(
                bounding_boxes=bounding_boxes,
                segmentations=None,
                frame=frame,
                rgb_colors=rgb_colors,
            )

        self.__add_frame_to_image_io(frame=annotated_frame)

    # TODO: type for rgb_colors
    def __run_model_on_image(
        self,
        model: ObjectDetectionModel[ConfigurationType, np.ndarray],  # type: ignore[type-arg]
        frame: np.ndarray,  # type: ignore[type-arg]
        rgb_colors: Any,
        file_path: Optional[str] = None,
    ) -> None:

        """
        Runs detection for single frame. If specified in config,
        generates annotation file from detections

        Args:
            model: Model which is used to detect objects
            frame: N-dimensional array representing single frame
            rgb_colors: List[Tuples(int, int, int)] specifying bounding box color
                        with len(List) == number of classes
            file_path: String of path of image/ video the frame belongs to

        Returns:
            None
        """

        annotation_path: str = ""

        if file_path is not None and self.config.write_output.annotation is not None:
            annotation_file_name = (
                self.config.write_output.annotation.output_file_name.replace(
                    FileNamePlaceholders.IMAGE_NAME,
                    os.path.basename(file_path)[:-4],
                )
            )

            annotation_path = os.path.join(
                self.config.write_output.annotation.output_dir,
                annotation_file_name,
            )

        if os.path.isfile(annotation_path):
            logger.info(
                "Already created annotation, skip run on image for annotation '%s'",
                annotation_path,
            )
        else:
            bounding_boxes: List[BoundingBox]

            _, bounding_boxes = model.predict(data_item=frame)

            self.__visualization_step(
                frame=frame,
                bounding_boxes=bounding_boxes,
                rgb_colors=rgb_colors,
            )

            if file_path is not None:
                if self.config.write_output.annotation is not None:
                    annotation_file_name = (
                        self.config.write_output.annotation.output_file_name.replace(
                            FileNamePlaceholders.IMAGE_NAME,
                            os.path.basename(file_path)[:-4],
                        )
                    )

                    annotation_path = os.path.join(
                        self.config.write_output.annotation.output_dir,
                        annotation_file_name,
                    )

                    # TODO: set image-dir and annotation-dir with sub-paths?
                    annotation = BaseAnnotation(
                        image_path=file_path,
                        annotation_path=annotation_path,
                        annotation_dir=self.config.write_output.annotation.output_dir,
                        image_dir=os.path.dirname(file_path),
                        image_shape=(frame.shape[0], frame.shape[1]),
                        classifications=[],
                        bounding_boxes=bounding_boxes,
                        segmentations=[],
                    )

                    # TODO: make allowed_classes configurable
                    annotation_to_xml(annotation=annotation, allowed_classes=None)

    def run_single_visualization_file_based(
        self, model: ObjectDetectionModel[ConfigurationType, np.ndarray]  # type: ignore[type-arg]
    ) -> None:

        """
        Wrapper function for running complete visualization step on input files

        Args:
            model: Model which is used to detect objects

        Returns:
            None
        """

        if self.file_paths is not None:
            rgb_colors = generate_detector_colors(num_classes=model.num_classes)

            self.__init_image_io()

            process_bar = tqdm(
                self.file_paths, desc=f"Run Inference for {model.get_name()}"
            )

            for counter, file_path in enumerate(process_bar):

                if (
                    self.config.input_data.images is not None
                    and counter < self.config.input_data.images.start_frame
                ):
                    continue
                if (
                    self.config.input_data.images is not None
                    and counter > self.config.input_data.images.stop_frame
                ):
                    break

                frame = cv2.imread(file_path)

                self.__run_model_on_image(
                    model=model, frame=frame, rgb_colors=rgb_colors, file_path=file_path
                )

                if (
                    self.video_live_output is not None
                    and self.video_live_output.is_terminated()
                ):
                    break

            self.__write_image_io()

    def run_single_visualization_video_based(
        self, model: ObjectDetectionModel[ConfigurationType, np.ndarray]  # type: ignore[type-arg]
    ) -> None:

        """
        Wrapper function for running complete visualization step on input videos

        Args:
            model: Model which is used to detect objects

        Returns:
            None
        """

        if self.video_file_input is not None:
            rgb_colors = generate_detector_colors(num_classes=model.num_classes)

            self.__init_image_io()

            # TODO: process_bar for video
            for counter, frame in enumerate(self.video_file_input.next_frame()):
                if not frame:
                    continue

                if (
                    self.config.input_data.video is not None
                    and counter < self.config.input_data.video.start_frame
                ):
                    continue
                if (
                    self.config.input_data.video is not None
                    and counter > self.config.input_data.video.stop_frame
                ):
                    break

                self.__run_model_on_image(
                    model=model, frame=frame, rgb_colors=rgb_colors
                )

                if self.config.input_data.video is not None:
                    self.video_file_input.skip_frames(
                        number_frames=self.config.input_data.video.skip_images
                    )

                if (
                    self.video_live_output is not None
                    and self.video_live_output.is_terminated()
                ):
                    break

            self.__write_image_io()

    def run_visualization(self) -> None:
        """
        Wrapper function for running all types of visualization
        """

        for model_config in self.config.model_configs:
            model: Model[PredictionType, ConfigurationType, DataType]  # type: ignore

            model = self.model_registry.init_model(model_config=model_config)
            assert isinstance(model, ObjectDetectionModel)

            self.run_single_visualization_file_based(model=model)
            self.run_single_visualization_video_based(model=model)


def main() -> None:
    _, project_root, _ = get_project_path_information(
        file_path=__file__, dir_depth=3, code_base="mlcvzoo_base"
    )

    Logger.init_logging_basic(
        log_dir=os.path.join(project_root, "logs"),
        log_file_postfix="ObjectDetectionVisualizer",
        no_stdout=False,
        root_log_level=logging.DEBUG,
        file_log_level=logging.DEBUG,
        stdout_log_level=logging.INFO,
    )

    visualizer = ObjectDetectionVisualizer()

    visualizer.run_visualization()


if __name__ == "__main__":
    main()
