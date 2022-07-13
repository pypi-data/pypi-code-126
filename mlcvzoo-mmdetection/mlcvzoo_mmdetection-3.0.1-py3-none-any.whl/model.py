# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Model that wraps all objection detection models of mmdetection
"""

import copy
import importlib
import logging
import os
import shlex
import subprocess
import sys
import typing
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union

import mlflow
import numpy as np
import torch.nn
from config_builder.replacement_map import get_replacement_map_copy
from mlcvzoo_base.api.data.bounding_box import BoundingBox
from mlcvzoo_base.api.data.class_identifier import ClassIdentifier
from mlcvzoo_base.api.interfaces import NetBased, Trainable
from mlcvzoo_base.api.model import ObjectDetectionModel
from mlcvzoo_base.configuration.replacement_config import ReplacementConfig
from mlcvzoo_base.configuration.structs import ObjectDetectionBBoxFormats
from mlcvzoo_base.configuration.utils import (
    create_configuration as create_basis_configuration,
)
from mlcvzoo_base.data_preparation.AnnotationClassMapper import AnnotationClassMapper
from mmcv import runner
from mmcv.utils import Registry
from mmdet.apis import inference_detector, init_detector

from mlcvzoo_mmdetection.configuration import MMDetectionConfig
from mlcvzoo_mmdetection.utils import get_mmdet_argparse_list, init_mmdetection_config

logger = logging.getLogger(__name__)


class MMDetectionModel(
    ObjectDetectionModel[MMDetectionConfig, Union[str, np.ndarray]],  # type: ignore[type-arg]
    NetBased[torch.nn.Module],
    Trainable,
):
    """
    Class for wrapping mmdetection models
    """

    def __init__(
        self,
        from_yaml: Optional[str] = None,
        configuration: Optional[MMDetectionConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        init_for_inference: bool = False,
        is_multi_gpu_instance: bool = False,
    ) -> None:

        self.net: Optional[torch.nn.Module] = None

        self.yaml_config_path: Optional[str] = from_yaml
        self.is_multi_gpu_instance: bool = is_multi_gpu_instance

        self.configuration: MMDetectionConfig = MMDetectionModel.create_configuration(
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )

        ObjectDetectionModel.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
        )

        if init_for_inference:
            self.__initialize_net()

        NetBased.__init__(self, net=self.net)
        Trainable.__init__(self)

        self.mapper = AnnotationClassMapper(
            class_mapping=self.configuration.class_mapping,
            reduction_mapping=self.configuration.inference_config.reduction_class_mapping,
        )

    def get_net(self) -> Optional[torch.nn.Module]:
        return self.net

    @property
    def num_classes(self) -> int:
        return self.mapper.num_classes

    def get_classes_id_dict(self) -> Dict[int, str]:
        return self.mapper.annotation_class_id_to_model_class_name_map

    def __initialize_net(self) -> None:

        cfg, self.configuration.inference_config.config_path = init_mmdetection_config(
            config_path=self.configuration.inference_config.config_path,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        if self.configuration.train_config.argparse_config.cfg_options is not None:
            cfg.merge_from_dict(
                self.configuration.train_config.argparse_config.cfg_options
            )

        logger.info(
            "Load model for %s from %s",
            self.get_name(),
            self.configuration.inference_config.checkpoint_path,
        )

        self.net = init_detector(
            config=cfg,
            checkpoint=self.configuration.inference_config.checkpoint_path,
            device=self.configuration.inference_config.device_string,
        )

    def save_reduced_checkpoint(
        self, input_checkpoint_path: str, output_checkpoint_path: str
    ) -> None:
        """
        Saves a reduced version of a stored checkpoint that does not contain optimizer states
        anymore. Therefore, it keeps the weights and meta information of the source checkpoint.

        Args:
            input_checkpoint_path: Path to source checkpoint file
            output_checkpoint_path: Path to where the checkpoint is saved
        """

        # loading config of current model
        cfg, _ = init_mmdetection_config(
            config_path=self.configuration.inference_config.config_path,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        # load checkpoint from source directory to a model
        model = init_detector(
            config=cfg,
            checkpoint=input_checkpoint_path,
            device=self.configuration.inference_config.device_string,
        )

        # Load input checkpoint dict from and extract the metadata for the output checkpoint.
        # Save reduced checkpoint with metadata of full checkpoint to target directory.
        runner.checkpoint.save_checkpoint(
            model,
            output_checkpoint_path,
            meta=runner.load_checkpoint(
                model, input_checkpoint_path, map_location="cpu"
            )["meta"],
        )

        logger.info(
            "Saved checkpoint from '%s' in a reduced version to '%s'.",
            input_checkpoint_path,
            output_checkpoint_path,
        )

    @staticmethod
    def create_configuration(
        from_yaml: Optional[str] = None,
        configuration: Optional[MMDetectionConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> MMDetectionConfig:
        return typing.cast(
            MMDetectionConfig,
            create_basis_configuration(
                configuration_class=MMDetectionConfig,
                from_yaml=from_yaml,
                input_configuration=configuration,
                string_replacement_map=string_replacement_map,
            ),
        )

    def __decode_mmdet_result(
        self, model_result: List[np.ndarray]  # type: ignore[type-arg]
    ) -> List[BoundingBox]:
        """
        Decode output of an object detection model from mmdetection

        Args:
            model_result: The result that the model has predicted

        Returns:
            The model_result as list of bounding boxes in MLCVZoo format
        """

        bounding_boxes: List[BoundingBox] = list()

        np_bounding_boxes = np.vstack(model_result)
        assert np_bounding_boxes.shape[1] == 5

        # Create numpy array containing all class ids
        class_id_list = []
        for index, box in enumerate(model_result):
            class_id_list.append(np.full(box.shape[0], index, dtype=np.int32))
        np_class_id_array = np.concatenate(class_id_list)

        # Get relevant indices that do match a given threshold
        np_scores = np_bounding_boxes[:, -1]
        valid_indices = np_scores > self.configuration.inference_config.score_threshold

        # Filter results according to the determined valid indices
        np_bounding_boxes = np_bounding_boxes[valid_indices, :]
        np_class_id_array = np_class_id_array[valid_indices]
        np_scores = np_scores[valid_indices]

        for bbox, class_id, score in zip(
            np_bounding_boxes, np_class_id_array, np_scores
        ):
            bbox_int = bbox.astype(np.int32)

            bounding_boxes.extend(
                self.build_bounding_boxes(
                    box_format=ObjectDetectionBBoxFormats.XYXY,
                    box_list=[bbox_int[0], bbox_int[1], bbox_int[2], bbox_int[3]],
                    class_identifiers=self.mapper.map_model_class_id_to_output_class_identifier(
                        class_id=class_id
                    ),
                    model_class_identifier=ClassIdentifier(
                        class_id=class_id,
                        class_name=self.mapper.map_annotation_class_id_to_model_class_name(
                            class_id=class_id
                        ),
                    ),
                    score=float(score),
                    difficult=False,
                    occluded=False,
                    content="",
                )
            )

        return bounding_boxes

    def predict(
        self, data_item: Union[str, np.ndarray]  # type: ignore[type-arg]
    ) -> Tuple[Union[str, np.ndarray], List[BoundingBox]]:  # type: ignore[type-arg]
        """
        Predicts objects for given data_item

        Args:
            data_item: Object on which a prediction is to be executed

        Returns:
            Data_item which served as input
            List of BoundingBox objects containing bounding box information for every prediction
            made by the model. Only contains bounding boxes which are above the score threshold
            specified in configuration file.
        """

        if self.net is None:
            self.__initialize_net()

        result = inference_detector(model=self.net, imgs=data_item)

        # Check if model output is only bbox head, or if the model has other heads:
        # tuple => bbox-head + mask-head
        if isinstance(result, tuple):
            model_result = result[0]

        # type is list => bbox-head only
        else:
            model_result = result

        bounding_boxes = self.__decode_mmdet_result(model_result=model_result)

        return data_item, bounding_boxes

    def train(self) -> None:

        if (
            ReplacementConfig.MMDETECTION_DIR_KEY
            not in self.configuration.string_replacement_map
        ):
            raise ValueError(
                f"Please provide a valid value "
                f"for the key '{ReplacementConfig.MMDETECTION_DIR_KEY}' "
                f"in your replacement configuration file."
            )

        mmdetection_dir = self.configuration.string_replacement_map[
            ReplacementConfig.MMDETECTION_DIR_KEY
        ]

        if self.configuration.train_config.argparse_config.launcher == "none":
            self.__run_training(mmdetection_dir=mmdetection_dir)
        else:
            self.__run_multi_gpu_training(mmdetection_dir=mmdetection_dir)

    def __setup_mlflow(self) -> None:
        # TODO: setup mlflow with MLFlowRunner

        pass

    @staticmethod
    def __register_dataset() -> None:
        """
        Register the custom dataset "CSVDataset" of the MLCVZoo in the registry of mmcv

        Returns:
            None
        """

        # IMPORTANT NOTE: Don't remove this import! It is later on used to be imported in the
        #                 mmdetection dataset registry
        from mlcvzoo_mmdetection.csv_dataset import CSVDataset

        DATASETS = Registry("dataset")
        DATASETS.register_module("CSVDataset")

    @staticmethod
    def run_mmdet_train(mmdetection_dir: str) -> None:
        """
        Call training script of the mmdet repository. Since the tools package is
        not part of their sources, it has to be called utilizing importlib python package

        Args:
            mmdetection_dir: Path to the mmdetection repository

        Returns:
            None
        """

        MMDetectionModel.__register_dataset()

        module_name = "train"

        # Clear module import
        if module_name in sys.modules:
            del sys.modules[module_name]

        mmdet_train_module_dir = os.path.join(mmdetection_dir, "tools")

        logger.info("Load mmdet train module from path: %s", mmdet_train_module_dir)

        sys_path_copy = copy.deepcopy(sys.path)
        # Set PYTHONPATH to only contain the relevant directory for the importlib call
        sys.path = [mmdet_train_module_dir]

        mmdet_train_module = importlib.import_module(module_name)

        # Revert modifications to the PYTHONPATH
        sys.path = sys_path_copy

        # Run the mmdet training
        mmdet_train_module.main()

    @staticmethod
    def __set_string_replacement_dict_in_cfg(
        cfg_options: Optional[Dict[str, Any]], string_replacement_map: Dict[str, str]
    ) -> Optional[Dict[str, Any]]:
        """
        Takes a dictionary representing the train_config.cfg_options of the MMDetectionConfig
        and sets the data.{train_step}.string_replacement_map_string_list if a
        data.{train_step}.annotation_handler_config_path is present. This is needed in order
        to make the string replacement available in the CSVDataset that the MLCVZoo adds to
        the mmdetection framework.

        Returns:
            The modified cfg_options dictionary
        """

        train_steps = ["train", "val", "test"]

        for train_step in train_steps:
            if (
                cfg_options is not None
                and f"data.{train_step}.annotation_handler_config_path"
            ):
                # TODO: add string_replacement json string
                cfg_options[
                    f"data.{train_step}.string_replacement_map_string_list"
                ] = "".join(dumps(string_replacement_map))

        return cfg_options

    def __run_training(self, mmdetection_dir: str) -> None:
        """
        Run mmdet training.

        Args:
            mmdetection_dir: Directory where the mmdetection repository has been cloned to.
                             This is needed to be able to call there tools/train.py script.

        Returns:
            None
        """

        argparse_config = self.configuration.train_config.argparse_config

        _, new_config_path = init_mmdetection_config(
            config_path=argparse_config.config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        argparse_config.cfg_options = self.__set_string_replacement_dict_in_cfg(
            cfg_options=argparse_config.cfg_options,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        if argparse_config.launcher == "none":
            argv_list = [
                sys.argv[0],
                new_config_path,
            ]
        else:
            argv_list = sys.argv.copy()

        argv_list.extend(
            get_mmdet_argparse_list(
                argparse_config=argparse_config,
                string_replacement_map=self.configuration.string_replacement_map,
            )
        )

        logger.info("Set sys.argv to: %s", sys.argv)

        sys.argv = argv_list

        MMDetectionModel.run_mmdet_train(mmdetection_dir=mmdetection_dir)

        mlflow.end_run()

    def __run_multi_gpu_training(self, mmdetection_dir: str) -> None:
        """
        Run mmdet multi-gpu/distributed training.

        Args:
            mmdetection_dir: Directory where the mmdetection repository has been cloned to.
                             This is needed to be able to call there tools/train.py script.

        Returns:
            None
        """

        assert self.configuration.train_config.multi_gpu_config is not None

        if (
            ReplacementConfig.MLCVZOO_DIR_KEY
            not in self.configuration.string_replacement_map
        ):
            raise ValueError(
                f"Please provide a valid value "
                f"for the key '{ReplacementConfig.MLCVZOO_DIR_KEY}' "
                f"in your replacement configuration file."
            )

        mlcvzoo_dir = self.configuration.string_replacement_map[
            ReplacementConfig.MLCVZOO_DIR_KEY
        ]

        cuda_visible_devices = (
            self.configuration.train_config.multi_gpu_config.cuda_visible_devices
        )
        gpus = self.configuration.train_config.argparse_config.gpus
        port = self.configuration.train_config.multi_gpu_config.multi_gpu_sync_port

        mlcvzoo_src_dir = os.path.join(mlcvzoo_dir, "src")

        env = os.environ.copy()
        env[
            "PYTHONPATH"
        ] = f"{os.environ.get('PYTHONPATH') if os.environ.get('PYTHONPATH') is not None else ''}"
        env["PYTHONPATH"] += f":{mlcvzoo_dir}"
        env["PYTHONPATH"] += f":{mlcvzoo_src_dir}"
        env["PYTHONPATH"] += f":{mmdetection_dir}"

        env["cuda_visible_devices"] = cuda_visible_devices

        for key, value in get_replacement_map_copy().items():
            env[key] = value

        _, new_config_path = init_mmdetection_config(
            config_path=self.configuration.train_config.argparse_config.config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        argv_list = get_mmdet_argparse_list(
            argparse_config=self.configuration.train_config.argparse_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        command = (
            f"-m torch.distributed.run "
            f"--nproc_per_node={gpus} "
            f"--master_port={port} "
            f"{__file__} "
            f"{new_config_path} "
        )

        for argv_parameter in argv_list:
            command += str(argv_parameter) + " "

        command += f"{mmdetection_dir} "

        logger.debug("Run command: %s", command)

        command_split = [sys.executable]
        command_split.extend(shlex.split(command))
        result = subprocess.run(args=command_split, env=env, check=False)

        if result.returncode:
            logger.error(
                "Command '%s' returned with exit code %i", command, result.returncode
            )
            raise RuntimeError(
                f"Distributed training exited with exitcode != 0, "
                f"exitcode: {result.returncode}"
            )
