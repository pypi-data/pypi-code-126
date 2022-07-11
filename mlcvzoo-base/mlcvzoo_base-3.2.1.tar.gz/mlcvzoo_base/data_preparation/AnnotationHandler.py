# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

""" Module for handling annotations according to configuration"""
import copy
import logging
import typing
import xml.etree.ElementTree as ET_xml
from typing import Any, Dict, List, Optional, Tuple

from config_builder.ConfigBuilder import ConfigBuilder

from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.configuration.AnnotationHandlerConfig import AnnotationHandlerConfig
from mlcvzoo_base.data_preparation.annotation_parser.coco_annotation_parser import (
    COCOAnnotationParser,
)
from mlcvzoo_base.data_preparation.annotation_parser.csv_annotation_parser import (
    CSVAnnotationParser,
)
from mlcvzoo_base.data_preparation.annotation_parser.cvat_annotation_parser import (
    CVATAnnotationParser,
)
from mlcvzoo_base.data_preparation.annotation_parser.pascal_voc_annotation_parser import (
    PascalVOCAnnotationParser,
)
from mlcvzoo_base.data_preparation.annotation_writer.csv_annotation_writer import (
    CSVAnnotationWriter,
)
from mlcvzoo_base.data_preparation.annotation_writer.darknet_annotation_writer import (
    DarknetAnnotationWriter,
)
from mlcvzoo_base.data_preparation.AnnotationClassMapper import AnnotationClassMapper
from mlcvzoo_base.data_preparation.data_classes.object_detection.DatasetInfo import (
    BaseDatasetInfo,
)
from mlcvzoo_base.data_preparation.structs import CSVOutputStringFormats

logger = logging.getLogger(__name__)


class AnnotationHandler:
    """Class for handling annotations"""

    csv_directory_replacement_string = "IMAGE_DIR_{}"
    csv_base_file_name: str

    def __init__(
        self,
        configuration: Optional[AnnotationHandlerConfig] = None,
        yaml_config_path: Optional[str] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> None:
        """

        Args:
            configuration: AnnotationHandlerConfig object
            yaml_config_path: path to configuration in yaml format
            mutual_attribute_map: dictionary mapping of AnnotationHandlerConfig to strings
            no_checks: whether to check for errors during the build of the configuration
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        """

        try:
            logger.info(
                "\nBuild AnnotationHandlerConfig from \n"
                "  - config path: '%s'\n"
                "  - config: '%s'",
                yaml_config_path,
                configuration,
            )

            config_builder = ConfigBuilder(
                class_type=AnnotationHandlerConfig,
                configuration=configuration,
                yaml_config_path=yaml_config_path,
                argparse_module_description="Load annotation in a variety of formats.",
                mutual_attribute_map=mutual_attribute_map,
                no_checks=no_checks,
                string_replacement_map=string_replacement_map,
            )

        except ValueError as ve:
            logger.error(ve)
            raise ve

        self.config: AnnotationHandlerConfig = typing.cast(
            AnnotationHandlerConfig, copy.deepcopy(config_builder.configuration)
        )

        self.mapper = AnnotationClassMapper(class_mapping=self.config.class_mapping)

        self.train_info_dict: Dict[str, Any] = {}
        self.eval_info_dict: Dict[str, Any] = {}

        self.list_splits: List[Tuple[List[str], BaseDatasetInfo]] = []

        self.replace_data_dirs: Dict[str, str] = dict()

    @property
    def num_classes(self) -> int:
        """

        Returns:
            Number of classes the AnnotationHandler considers
        """
        return self.mapper.num_classes

    def parse_annotations_from_xml(self) -> List[BaseAnnotation]:
        """
        Creates a list of annotations using the configuration
        given via pascal_voc_input_data

        Returns:
            The created list
        """

        pascal_voc_parser = PascalVOCAnnotationParser(
            mapper=self.mapper, pascal_voc_input_data=self.config.pascal_voc_input_data
        )

        annotations: List[BaseAnnotation] = pascal_voc_parser.parse()

        return annotations

    def parse_annotations_from_coco(self) -> List[BaseAnnotation]:
        """

        Returns: List of BaseAnnotations read from a coco formatted file (json)

        """

        coco_parser = COCOAnnotationParser(
            mapper=self.mapper, coco_input_data=self.config.coco_input_data
        )

        annotations: List[BaseAnnotation] = coco_parser.parse()

        return annotations

    def parse_annotations_from_cvat(self) -> List[BaseAnnotation]:
        """

        Returns: List of BaseAnnotations read from a cvat formatted file (xml)

        """

        cvat_parser = CVATAnnotationParser(
            mapper=self.mapper, cvat_input_data=self.config.cvat_input_data
        )

        annotations: List[BaseAnnotation] = cvat_parser.parse()

        return annotations

    def parse_meta_info_from_cvat(self) -> List[ET_xml.Element]:
        """
        Returns:
            List of XMLElement objects that build the meta information in a CVAT formatted file
        """

        cvat_parser = CVATAnnotationParser(
            mapper=self.mapper, cvat_input_data=self.config.cvat_input_data
        )
        meta_info: List[ET_xml.Element] = cvat_parser.parse_cvat_meta_info()

        return meta_info

    def parse_annotations_from_csv(
        self,
        csv_file_path: str,
    ) -> List[BaseAnnotation]:
        """
        Create a dict of annotation information to a corresponding csv file
        The keys are the names of the classes_name_dict given by the classes_name_dict.
        Additionally there ist one key 'list' which stores a list of objects
        of the "BaseAnnotation" class

        Args:
            csv_file_path: path to csv file

        Returns:
            A List of BaseAnnotations which are loaded from the given csv

        """

        csv_parser = CSVAnnotationParser(
            mapper=self.mapper,
            csv_file_path=csv_file_path,
            pascal_voc_input_data=self.config.pascal_voc_input_data,
            coco_input_data=self.config.coco_input_data,
            cvat_input_data=self.config.cvat_input_data,
        )

        annotations: List[BaseAnnotation] = csv_parser.parse()

        return annotations

    def generate_darknet_train_set(self, annotations: List[BaseAnnotation]) -> None:
        """
        Generate the dataset for the Darknet framework. It consists of two sets of images
        alongside with text files containing the annotations, one .txt per image. Two files,
        train.txt and test.txt, contain the list of image files.

        Args:
            annotations: List of BaseAnnotations from which training data is derived

        Returns:
            None
        """

        if self.config.write_output is None or (
            self.config.write_output is not None
            and self.config.write_output.darknet_train_set is None
        ):
            raise ValueError(
                "The write_output config is None! In order to be able to generate a darknet "
                "training set the write_output and write_output.darknet_train_set have to be "
                "provided!"
            )

        darknet_annotation_writer = DarknetAnnotationWriter(
            darknet_train_set_config=self.config.write_output.darknet_train_set,
            split_size=self.config.write_output.split_size,
        )

        _ = darknet_annotation_writer.write(annotations=annotations)

    def generate_csv(
        self,
        annotations: List[BaseAnnotation],
        output_string_format: str = CSVOutputStringFormats.BASE,
    ) -> Optional[str]:
        """
        Generate a csv file based on the given AnnotationHandler config.
        The generation is based on given directories for parsing image and annotation paths.
        Currently only .xml annotation files in PASCAL-VOC format are supported.

        Args:
            annotations: List of BaseAnnotations which are about to be transformed to csv format
            output_string_format: Format of generated csv string (one of CSVOutputStringFormats)

        Returns:
            Optional, path to the generated csv
        """

        assert self.config.write_output is not None
        assert self.config.write_output.csv_annotation is not None

        csv_annotation_writer = CSVAnnotationWriter(
            write_output_config=self.config.write_output,
            output_string_format=output_string_format,
        )

        output_file_path: Optional[str] = csv_annotation_writer.write(
            annotations=annotations
        )

        return output_file_path

    def parse_from_all_source(self) -> List[BaseAnnotation]:
        """
        Parse annotations from all different types of annotation formats that are provided
        by the CVAT export/import functionality. By setting the merge_content parameter to True,
        all annotations are merged on the basis of the image_path
        (which should be a unique identifier).

        Returns: a List of BaseAnnotations
        """

        annotations: List[BaseAnnotation] = []

        annotations.extend(self.parse_annotations_from_xml())
        annotations.extend(self.parse_annotations_from_coco())
        annotations.extend(self.parse_annotations_from_cvat())

        return annotations
