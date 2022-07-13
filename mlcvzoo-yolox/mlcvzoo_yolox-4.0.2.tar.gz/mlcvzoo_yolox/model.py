# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module that defines a wrapper class for yolox:
https://github.com/Megvii-BaseDetection/YOLOX/
"""

import argparse
import importlib
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union, cast

import numpy as np
import torch
from mlcvzoo_base.api.data.bounding_box import BoundingBox
from mlcvzoo_base.api.interfaces import NetBased, Trainable
from mlcvzoo_base.api.model import ObjectDetectionModel
from mlcvzoo_base.configuration.utils import (
    create_configuration as create_basis_configuration,
)
from mlcvzoo_base.data_preparation.AnnotationClassMapper import AnnotationClassMapper
from yolox.core import launch
from yolox.data import ValTransform
from yolox.exp.build import get_exp
from yolox.utils import fuse_model, get_num_devices

from mlcvzoo_yolox.configuration import YOLOXConfig
from mlcvzoo_yolox.exp.custom_yolox_exp import CustomYOLOXExp
from mlcvzoo_yolox.model_utils import predict_with_model
from mlcvzoo_yolox.third_party.yolox.tools.train import main as train_yolox
from mlcvzoo_yolox.third_party.yolox.tools.trt import convert_to_tensorrt

logger = logging.getLogger(__name__)


class YOLOXModel(
    ObjectDetectionModel[YOLOXConfig, Union[str, np.ndarray, torch.Tensor]],  # type: ignore[type-arg]
    NetBased[torch.nn.Module],
    Trainable,
):
    """
    Class to wrap the implementation of yolox
    """

    def __init__(
        self,
        from_yaml: Optional[str] = None,
        configuration: Optional[YOLOXConfig] = None,
        init_for_inference: bool = False,
        string_replacement_map: Optional[Dict[str, str]] = None,
        load_tensorrt_model: bool = False,
    ) -> None:
        """
        Construct a YOLOXModel

        Args:
            from_yaml: (Optional) The yaml path where to parse the YOLOXConfig from
            configuration: (Optional) An ready to use YOLOXConfig object
            init_for_inference: If the YOLOXModel should be used for inference
            string_replacement_map: A dictionary that provides placeholders information that
                                    is needed to build a YOLOXConfig utilizing the ConfigBuilder
            load_tensorrt_model: If the YOLOXModel should use a tensorrt model instead of torch
        """

        self.yaml_config_path = from_yaml
        self.init_for_inference = init_for_inference

        self.configuration: YOLOXConfig = YOLOXModel.create_configuration(
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )
        ObjectDetectionModel.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
        )

        self.mapper = AnnotationClassMapper(
            class_mapping=self.configuration.class_mapping
        )

        self.exp: CustomYOLOXExp = CustomYOLOXExp(
            configuration=self.configuration,
        )
        self.decode_output: bool = False
        self.preprocess: Optional[ValTransform] = None

        self.net: Optional[torch.nn.Module] = None
        if self.init_for_inference:
            self.init_inference_model(load_tensorrt_model=load_tensorrt_model)

        NetBased.__init__(self, net=self.net)
        Trainable.__init__(self)

    @property
    def num_classes(self) -> int:
        return int(self.exp.num_classes)

    def get_classes_id_dict(self) -> Dict[int, str]:
        return self.exp.mapper.annotation_class_id_to_model_class_name_map

    def get_net(self) -> Optional[torch.nn.Module]:
        return self.net

    @staticmethod
    def create_configuration(
        from_yaml: Optional[str] = None,
        configuration: Optional[YOLOXConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> YOLOXConfig:
        return cast(
            YOLOXConfig,
            create_basis_configuration(
                configuration_class=YOLOXConfig,
                from_yaml=from_yaml,
                input_configuration=configuration,
                string_replacement_map=string_replacement_map,
            ),
        )

    # TODO: make this static so that is can be used in the MLCVZooEvaluator for yolox evaluations
    #       during training
    def init_inference_model(self, load_tensorrt_model: bool = False) -> None:
        """
        Initializes the neural network of the YOLOXModel. It either loads a
        torch module or a tensorrt module (torch2trt). The respective weights
        are taken from the YOLOXConfiguration of the YOLOXModel.

        Returns:
            None
        """
        self.preprocess = ValTransform(
            legacy=self.configuration.inference_config.legacy
        )

        del self.net
        self.net = None

        # Execute the TensorRT model if configuration exists and all required files are there
        # If they are not present the conversion must be run first
        if not load_tensorrt_model or self.configuration.trt_config is None:
            self.net = self.exp.get_model()

            if self.configuration.inference_config.device == "gpu":
                self.net.cuda()
                if self.configuration.inference_config.gpu_fp16:
                    self.net.half()  # to FP16
            self.net.eval()

            self.load_checkpoint(
                checkpoint_path=self.configuration.inference_config.checkpoint_path
            )
        else:
            # NOTE: TensorRT only works with gpu / CUDA
            self.configuration.inference_config.device = "gpu"

            self.decode_output = True
            self.load_trt_checkpoint(
                checkpoint_path=self.configuration.trt_config.trt_checkpoint_path
            )

    def load_trt_checkpoint(self, checkpoint_path: str) -> None:
        """
        Load the checkpoint for the model

        Returns:
            None
        """
        try:
            # TensorRT is optional, so imported here
            # pylint: disable=C0415
            from torch2trt import TRTModule
        except ImportError as importerror:
            logger.error("Torch2TRT is not installed, no model checkpoint loaded.")
            raise importerror

        logger.info("Load model (trt) checkpoint from: %s", checkpoint_path)

        tensorrt_module = TRTModule()
        state_dict = torch.load(checkpoint_path)  # type: ignore[no-untyped-call]
        tensorrt_module.load_state_dict(state_dict=state_dict)
        self.net = tensorrt_module

    def load_checkpoint(self, checkpoint_path: str) -> None:
        """
        Load the checkpoint for the model

        Returns:
            None
        """

        if self.configuration.inference_config.fuse:
            self.net = fuse_model(self.net)

        if not os.path.isfile(checkpoint_path):
            raise ValueError(
                f"The given checkpoint path does not exist! checkpoint_path: {checkpoint_path}"
            )

        ckpt = torch.load(checkpoint_path, map_location="cpu")  # type: ignore

        logger.info("Load model checkpoint from: %s", checkpoint_path)

        assert self.net is not None
        # load the model state dict
        self.net.load_state_dict(ckpt["model"])

    def convert_to_tensorrt(self) -> None:
        """
        Converts the stored torch model instance to tensorrt

        Returns:
            None
        """

        if self.net is None:
            raise ValueError("The net attribute has not yet been initialized!")

        convert_to_tensorrt(
            model=self.net,
            yolox_config=self.configuration,
        )

    def predict(
        self, data_item: Union[str, np.ndarray, torch.Tensor]  # type: ignore[type-arg]
    ) -> Tuple[Union[str, np.ndarray, torch.Tensor], List[BoundingBox]]:  # type: ignore[type-arg]
        """
        Run a yolox model on a given input image and predict a list of
        mlcvzoo conform bounding boxes

        Args:
            data_item: Either the path to an image or a already created numpy image

        Returns:
            The predicted bounding boxes
        """
        if self.net is None:
            raise ValueError("The net attribute has not yet been initialized!")

        return predict_with_model(
            model=self.net,
            data_item=data_item,
            preprocess=self.preprocess,
            inference_config=self.configuration.inference_config,
            decode_output=self.decode_output,
            strides=self.exp.strides,
            mapper=self.exp.mapper,
        )

    def __get_yolox_argparse_namespace(self) -> argparse.Namespace:
        """
        Load the yolox argparse arguments from the YOLOXTrainArgparseConfig configuration object

        We build the same argparse arguments as in yolox/tools/train.py this makes it easier to
        be compatible to their API.

        Returns:
            the created argparse Namespace
        """

        if self.configuration.train_config is None:
            raise ValueError(
                "train_config is None! In order to be able to train a yolox model"
                "a valid train_config has to be provided!"
            )

        argparse_dict: Dict[str, Any] = vars(
            self.configuration.train_config.argparse_config
        )

        # Fill out additional argparse parameters
        argparse_dict["experiment_name"] = self.configuration.experiment_config.exp_name
        argparse_dict["name"] = None

        args: argparse.Namespace = argparse.Namespace(**argparse_dict)

        return args

    def train(self) -> None:

        if self.configuration.train_config is None:
            raise ValueError(
                "train_config is None! In order to be able to train a yolox model"
                "a valid train_config has to be provided!"
            )

        if self.configuration.train_config.argparse_config.devices is not None:
            num_gpus = self.configuration.train_config.argparse_config.devices
        else:
            num_gpus = get_num_devices()

        assert num_gpus <= get_num_devices()

        if self.configuration.train_config.argparse_config.dist_url is not None:
            dist_url = self.configuration.train_config.argparse_config.dist_url
        else:
            dist_url = "auto"

        args = self.__get_yolox_argparse_namespace()

        launch(
            main_func=train_yolox,
            num_gpus_per_machine=num_gpus,
            num_machines=self.configuration.train_config.argparse_config.num_machines,
            machine_rank=self.configuration.train_config.argparse_config.machine_rank,
            backend=self.configuration.train_config.argparse_config.dist_backend,
            dist_url=dist_url,
            args=(self.exp, args),
        )
