# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for creating a look-up model based on existing annotations"""
import logging
import os
import typing
from abc import ABC
from typing import Dict, Generic, List, Optional, Tuple, TypeVar

from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.data.bounding_box import BoundingBox
from mlcvzoo_base.api.data.classification import Classification
from mlcvzoo_base.api.data.segmentation import Segmentation
from mlcvzoo_base.api.interfaces import Classifiable
from mlcvzoo_base.api.model import (
    ClassificationModel,
    Model,
    ObjectDetectionModel,
    SegmentationModel,
)
from mlcvzoo_base.configuration.utils import (
    create_configuration as create_basis_configuration,
)
from mlcvzoo_base.data_preparation.AnnotationHandler import AnnotationHandler
from mlcvzoo_base.models.read_from_file.configuration import ReadFromFileConfig

logger = logging.getLogger(__name__)

ModelType = TypeVar(
    "ModelType",
    ClassificationModel[ReadFromFileConfig, str],
    ObjectDetectionModel[ReadFromFileConfig, str],
    SegmentationModel[ReadFromFileConfig, str],
)


class ReadFromFileModel(
    Model,  # type: ignore
    Classifiable,
    ABC,
    Generic[ModelType],
):
    """
    Simple Model which can be used as fast Online detector.
    It takes an "AnnotationHandlerConfig" and parses all annotations
    based on this config into a datastructure. At prediction step it
    simply looks up the annotation based on the image-path information.

    NOTE: The ReadFromFileModel is only a 'Model'. In order to become a model of a
          dedicated type like ClassificationModel or ObjectDetectionModel, the
          Subclasses of a ReadFromFileModel have to inherit not only from the
          ReadFromFileModel but also from the dedicated type itself.

    NOTE: The constructor of the super class Model will not be called since
          the ReadFromFileModel is an abstract super class and therefore is
          not intended to be instantiated. But make sure to call the Model
          constructor in one of the implementing subclasses.
    """

    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[ReadFromFileConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ):
        self.annotations_dict: Dict[str, BaseAnnotation] = {}

        self.configuration: ReadFromFileConfig = ReadFromFileModel.create_configuration(
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )

        self.annotation_handler = AnnotationHandler(
            configuration=self.configuration.annotation_handler_config,
            string_replacement_map=string_replacement_map,
        )

        self.__read_data()

        Model.__init__(
            self,
            unique_name=os.path.basename(from_yaml).replace(".yaml", ""),
            configuration=self.configuration,
        )

        self.get_name()

    @staticmethod
    def create_configuration(
        from_yaml: Optional[str] = None,
        configuration: Optional[ReadFromFileConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> ReadFromFileConfig:
        return typing.cast(
            ReadFromFileConfig,
            create_basis_configuration(
                configuration_class=ReadFromFileConfig,
                from_yaml=from_yaml,
                input_configuration=configuration,
                string_replacement_map=string_replacement_map,
            ),
        )

    @property
    def num_classes(self) -> int:
        return self.annotation_handler.mapper.num_classes

    def get_classes_id_dict(self) -> Dict[int, str]:
        return (
            self.annotation_handler.mapper.annotation_class_id_to_model_class_name_map
        )

    def __read_data(self) -> None:

        annotations = self.annotation_handler.parse_from_all_source()

        self.annotations_dict = {}

        for annotation in annotations:

            if annotation.image_path in self.annotations_dict:
                logger.warning(
                    "Duplicate annotation data for image '%s'.\n"
                    "Check your annotation-handler configuration!",
                    annotation.image_path,
                )

            self.annotations_dict[annotation.image_path] = annotation


class ReadFromFileClassificationModel(
    ClassificationModel[ReadFromFileConfig, str],
    ReadFromFileModel[ClassificationModel[ReadFromFileConfig, str]],
):
    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[ReadFromFileConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ):
        ReadFromFileModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )
        ClassificationModel.__init__(
            self,
            unique_name=os.path.basename(from_yaml).replace(".yaml", ""),
            configuration=self.configuration,
        )

    def predict(self, data_item: str) -> Tuple[str, List[Classification]]:
        classifications: List[Classification] = list()

        if data_item in self.annotations_dict:
            classifications.extend(self.annotations_dict[data_item].classifications)

        return data_item, classifications


class ReadFromFileObjectDetectionModel(
    ObjectDetectionModel[ReadFromFileConfig, str],
    ReadFromFileModel[ObjectDetectionModel[ReadFromFileConfig, str]],
):
    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[ReadFromFileConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ):
        ReadFromFileModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )
        ObjectDetectionModel.__init__(
            self,
            unique_name=os.path.basename(from_yaml).replace(".yaml", ""),
            configuration=self.configuration,
        )

    def predict(self, data_item: str) -> Tuple[str, List[BoundingBox]]:
        bounding_boxes: List[BoundingBox] = list()

        include_segmentations: bool = self.configuration.include_segmentations

        if data_item in self.annotations_dict:
            bounding_boxes.extend(
                self.annotations_dict[data_item].get_bounding_boxes(
                    include_segmentations=include_segmentations
                )
            )

        return data_item, bounding_boxes


class ReadFromFileSegmentationModel(
    SegmentationModel[ReadFromFileConfig, str],
    ReadFromFileModel[SegmentationModel[ReadFromFileConfig, str]],
):
    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[ReadFromFileConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ):
        ReadFromFileModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )
        SegmentationModel.__init__(
            self,
            unique_name=os.path.basename(from_yaml).replace(".yaml", ""),
            configuration=self.configuration,
        )

    def predict(self, data_item: str) -> Tuple[str, List[Segmentation]]:
        segmentations: List[Segmentation] = list()

        if data_item in self.annotations_dict:
            segmentations.extend(self.annotations_dict[data_item].segmentations)

        return data_item, segmentations
