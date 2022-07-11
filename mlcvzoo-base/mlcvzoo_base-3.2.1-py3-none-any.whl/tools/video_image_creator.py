# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for extracting frames from videos"""
import argparse
import copy
import json
import logging
import os
import sys
import typing
from datetime import datetime
from typing import Dict, List, Optional

import cv2
import numpy as np
from config_builder.ConfigBuilder import ConfigBuilder

from mlcvzoo_base.tools.configuration.video_image_creator_config import (
    VideoImageCreatorConfig,
)
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils.file_utils import (
    ensure_dir,
    get_file_list,
    get_project_path_information,
)

logger = logging.getLogger("{}".format(__name__))


class VideoImageCreator:

    """
    Tool to step through video and manually sort out frames to use as training data.
    When executed, displays every frame in given video separately. User is able to
    execute following commands:
    - Exit: 'q', 'Q', 'Esc'
    - Save current frame as .jpg: 's'
    - Change step size: '1' for 1 step, '2' for step, ...

    (See ./config/templates/tools/video-image-creator_template.yaml for example)
    """

    MODES: List[str] = ["terminate", "run"]

    video_files: List[str]

    current_pos: int = 0
    current_frame: Optional[np.ndarray] = None  # type: ignore[type-arg]
    current_video_capture: Optional[cv2.VideoCapture] = None
    current_video_path: Optional[str] = None

    def __init__(self) -> None:

        self.args = self.parse_arguments()
        logger.debug("Arguments '%s'" % self.args)

        assert self.args.yaml_config_path is not None

        config_builder = ConfigBuilder(
            class_type=VideoImageCreatorConfig,
            yaml_config_path=self.args.yaml_config_path,
        )

        self.config: VideoImageCreatorConfig = typing.cast(
            VideoImageCreatorConfig, config_builder.configuration
        )

        logger.info(
            "\n========================================\n"
            "Start VideoImageCreator using config: \n\n"
            "%s\n\n"
            "========================================\n",
            config_builder.yaml_config_path,
        )

        self.step_width_map: Dict[int, int] = {}
        for key in self.config.step_width_map.keys():
            self.step_width_map[ord(key)] = self.config.step_width_map[key]

        self.mode = "run"

        self.frame = 0

        self.resized_window = False

        self.step_width = 1

        cv2.namedWindow(self.config.winname, cv2.WINDOW_NORMAL)

        self.video_files = []
        if os.path.isdir(self.config.video_input_dir):
            self.video_files.extend(
                get_file_list(
                    input_dir=self.config.video_input_dir,
                    search_subfolders=True,
                    file_extension=self.config.video_file_extension,
                )
            )
        elif os.path.isfile(self.config.video_input_path):
            self.video_files.append(self.config.video_input_path)
        else:
            logger.error(
                "Could not init a video file. Please provide a correct parameter for "
                " 'video_input_dir' or 'video_input_path'"
            )

        if len(self.video_files) == 0:
            logger.error("No videos found for the given configuration!")
            sys.exit(-1)
        else:
            logger.info("Input Video: ")
            self.__print_videos()

    def __print_videos(self) -> None:

        """
        Prints every video path specified in video_image_creator_yaml
        """
        for video_path in self.video_files:
            logger.info("  - %s", video_path)

    def parse_arguments(self) -> argparse.Namespace:

        """
        Parse arguments used by video image creator
        Returns:
            args: Parsed arguments

        """

        parser = argparse.ArgumentParser(
            description="Tool for generating training images from given video files"
        )

        parser.add_argument(
            "-y",
            "--yaml-config-path",
            type=str,
            help="Path to the yaml configuration file for this tool.",
        )

        args = parser.parse_args()

        return args

    def __output_frame(self, frame: Optional[np.ndarray]) -> bool:  # type: ignore[type-arg]

        """
        Displays current frame incl. information about video name,
        current frame number and video FPS. While displaying frame,
        user can change step size according to step_width_map provided
        in video_image_creator_config_yaml. Also, user can save the current
        frame as single .jpg by pressing 's'

        Args:
            frame: N-dimensional Array representing single frame of video

        Returns:
            modified_value: Boolean which indicates if step size has changed

        """

        modified_value = False

        if (
            self.current_video_path is not None
            and self.current_video_capture is not None
            and frame is not None
        ):

            output_frame = copy.deepcopy(frame)

            # will only be executed once
            if not self.resized_window:
                scale_factor = frame.shape[1] / frame.shape[0]

                if self.config.resize_window is True:
                    window_height = self.config.window_size
                else:
                    window_height = frame.shape[0]

                cv2.resizeWindow(
                    winname=self.config.winname,
                    height=window_height,
                    width=int(window_height * scale_factor),
                )

                self.resized_window = True

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Video: {os.path.basename(self.current_video_path)}",
                org=(20, 40),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Current frame number: {self.current_pos}/"
                f"{self.current_video_capture.get(cv2.CAP_PROP_FRAME_COUNT)}",
                org=(20, 80),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Video FPS: {self.current_video_capture.get(cv2.CAP_PROP_FPS)}",
                org=(20, 120),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            cv2.imshow(self.config.winname, output_frame)

            key = cv2.waitKey(0) & 0xFF
            if key in self.step_width_map.keys():
                logger.info("set step-width to %s", self.step_width_map[key])
                self.step_width = self.step_width_map[key]

                modified_value = True

            elif key == 27 or key == ord("q") or key == ord("Q"):
                self.close()
            elif key == ord("s"):
                logger.info("save image ...")
                self.__write_frame(frame=frame)
            else:
                logger.info("next image...")

            self.frame += 1

            del output_frame

        return modified_value

    def __write_frame(self, frame: Optional[np.ndarray]) -> None:  # type: ignore[type-arg]

        """
        Saves given frame as .jpg to same directory as input video

        Args:
            frame: N-dimensional Array representing single frame of video

        Returns:
            None
        """

        if (
            frame is not None
            and self.current_video_path is not None
            and self.current_video_capture is not None
        ):

            video_fps = self.current_video_capture.get(cv2.CAP_PROP_FPS)
            video_pos = self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES)

            timestamp = datetime.utcfromtimestamp(1 / video_fps * video_pos).strftime(
                "%H-%M-%S-%f"
            )

            video_name_base = os.path.basename(self.current_video_path).replace(
                self.config.video_file_extension, ""
            )

            output_path = os.path.join(
                os.path.dirname(self.current_video_path),
                video_name_base,
                f"{video_name_base}_{timestamp}.jpg",
            )

            if not os.path.isfile(output_path):
                ensure_dir(file_path=output_path, verbose=True)

                logger.info("Write image to %s", output_path)
                cv2.imwrite(output_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            else:
                logger.info("Image already exist at %s", output_path)

    def __reset(self) -> None:
        """
        Closes current video and resets current_video variables to None
        """

        if self.current_video_capture is not None:
            self.current_video_capture.release()

        self.current_video_capture = None
        self.current_video_path = None

        logger.info("Reset video. Videos left: ")
        self.__print_videos()

    def run(self) -> None:
        """
        Wrapper function for executing the video_image_creator
        """

        modified_value = False

        logger.info(
            "Press 'Esc', 'q' or 'Q' to exit.\n"
            "Press 's' for saving current frame.\n"
            "step_width_map: \n"
            "%s\n"
            "Press any other key to step through video.",
            json.dumps(obj=self.step_width_map, indent=2),
        )
        while self.mode != "terminate":

            if self.current_video_capture is None:
                if len(self.video_files) == 0:
                    self.mode = "terminate"
                    break
                else:
                    self.current_video_path = self.video_files.pop()

                    logger.info("Start with video %s", self.current_video_path)
                    self.current_video_capture = cv2.VideoCapture(
                        self.current_video_path
                    )

            if not modified_value:
                self.current_pos = (
                    self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES)
                    + self.step_width
                    - 1
                )
                self.goto_frame(frame_position=self.current_pos)

                logger.info(
                    "Read frame at position: %s",
                    self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES),
                )
                read, self.current_frame = self.current_video_capture.read()

                if not read:
                    logger.info("Video finished. Read new video ...")
                    self.__reset()
                    continue
            else:
                logger.info("stay at pos")

            modified_value = self.__output_frame(frame=self.current_frame)

    def goto_frame(self, frame_position: int) -> None:
        """
        Takes integer specifying which frame should be displayed
        next and sets the frame accordingly.

        Args:
            frame_position: Integer specifying which frame_position to be set next

        Returns:
            None
        """

        if self.current_video_capture is not None:
            frame_position = max(0, frame_position)

            logger.info("set frame position to %s", frame_position)
            self.current_video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_position)

    def __del__(self):  # type: ignore
        if self.current_video_capture is not None:
            self.current_video_capture.release()

    def close(self) -> None:

        """
        Destroys the current window
        """

        self.mode = "terminate"
        cv2.destroyAllWindows()


def main() -> None:

    _, project_root, _ = get_project_path_information(
        file_path=__file__, dir_depth=3, code_base="mlcvzoo_base"
    )

    Logger.init_logging_basic(
        log_dir=os.path.join(project_root, "logs"),
        log_file_postfix="VideoImageCreator",
        no_stdout=False,
        root_log_level=logging.DEBUG,
        file_log_level=logging.DEBUG,
        stdout_log_level=logging.INFO,
    )

    video_image_creator = VideoImageCreator()

    video_image_creator.run()


if __name__ == "__main__":
    main()
