# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for providing the possibility to train a mmdetection
model on data that is defined in a csv file. This is realized
by extending the 'DATASETS' registry of mmdetection.
"""

import logging
from typing import Any, Dict, List, Optional

import numpy as np
from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.configuration.AnnotationHandlerConfig import AnnotationHandlerConfig
from mlcvzoo_base.data_preparation.AnnotationHandler import AnnotationHandler
from mmdet.datasets.builder import DATASETS
from mmdet.datasets.custom import CustomDataset

from mlcvzoo_mmdetection.utils import parse_string_replacement_map

logger = logging.getLogger(__name__)


@DATASETS.register_module()
class CSVDataset(CustomDataset):

    """
    Implementation of a custom dataset. It follows the instructions given by:
    https://mmdetection.readthedocs.io/en/latest/tutorials/customize_dataset.html

    We followed an example and created our own dataset class
    which has to be compatible to the class "CustomDataset"
    of the mmdetection framework

    Custom dataset for bounding_box.

    Annotation format required from mmdet.datasets.custom.CustomDataset:
    [
        {
            'filename': 'a.jpg',
            'width': 1280,
            'height': 720,
            'ann': {
                'bboxes': <np.ndarray> (n, 4),
                'labels': <np.ndarray> (n, ),
                'bboxes_ignore': <np.ndarray> (k, 4), (optional field) => NOTE: not yet implemented
                'labels_ignore': <np.ndarray> (k, 4) (optional field)  => NOTE: not yet implemented
            }
        },
        ...
    ]

    The `ann` field is optional for testing.
    """

    def __init__(
        self,
        ann_file: Optional[
            str
        ],  # => ensure compatibility to superclass 'CustomDataset'
        pipeline: Optional[Any],
        classes: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        data_root: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        img_prefix: Optional[
            str
        ] = "",  # => ensure compatibility to superclass 'CustomDataset'
        seg_prefix: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        proposal_file: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        test_mode: bool = False,  # => ensure compatibility to superclass 'CustomDataset'
        filter_empty_gt: bool = True,  # => ensure compatibility to superclass 'CustomDataset'
        annotation_handler_config_path: str = "",
        annotation_handler_config: Optional[AnnotationHandlerConfig] = None,
        string_replacement_map_string_list: Optional[List[str]] = None,
        ann_file_list: Optional[List[str]] = None,
    ) -> None:
        # Needed for mmcv registry
        self.annotations: List[BaseAnnotation] = list()

        self.ann_file_list = ann_file_list

        string_replacement_map: Dict[str, str] = {}
        if string_replacement_map_string_list is not None:
            string_replacement_map = parse_string_replacement_map(
                string_replacement_map_string_list=string_replacement_map_string_list
            )

        self.annotation_handler = AnnotationHandler(
            yaml_config_path=annotation_handler_config_path,
            configuration=annotation_handler_config,
            string_replacement_map=string_replacement_map,
        )

        CustomDataset.__init__(
            self,
            ann_file,
            pipeline,
            classes=None,
            data_root=None,
            img_prefix="",
            seg_prefix=None,
            proposal_file=None,
            test_mode=False,
            filter_empty_gt=True,
        )

        self.flag = np.ones(len(self), dtype=np.uint8)

        self.CLASSES = self.annotation_handler.mapper.get_model_class_names()

        logger.info("Finished CSVDataset init ...")

        # TODO: remove, is called by super constructor?!
        # load annotations (and proposals)
        # self.data_infos = self.load_annotations(None)

        # TODO: Needed?
        # self.ann_file = None
        # self.data_root = None
        # self.img_prefix = ""
        # self.seg_prefix = None
        # self.proposal_file = None
        # self.test_mode = False
        # self.filter_empty_gt = False

        # TODO: remove, is called by super constructor?!
        # processing pipeline
        # self.pipeline = Compose(pipeline)

    def __len__(self):  # type: ignore
        return len(self.data_infos)

    def load_annotations(self, ann_file) -> List:  # type: ignore
        """
        Overwrite from 'CustomDataset'.

        Parse all annotation data from the configured csv-files and save it to a Dict
        which is in the 'CustomDataset' format

        :param:
        """
        img_infos = []

        if self.ann_file_list is not None:
            for csv_file_path in self.ann_file_list:
                self.annotations.extend(
                    self.annotation_handler.parse_annotations_from_csv(
                        csv_file_path=csv_file_path
                    )
                )

            for i, annotation in enumerate(self.annotations):

                # Dict structure is based on 'CustomDataset'
                info = dict(
                    height=annotation.get_height(),
                    width=annotation.get_width(),
                    filename=annotation.image_path,
                )

                img_infos.append(info)

        return img_infos

    def get_ann_info(self, idx: int) -> Dict[str, Any]:
        """
        Overwrite from 'CustomDataset' to get the annotations for mmdetection in the correct format

        """

        gt_bboxes = []
        gt_labels = []

        annotation = self.annotations[idx]
        logger.debug(
            "Load annotation via get_ann_info for index %s: \n"
            "  - annotation.image_path: "
            "%s\n"
            "  - annotation.bbox:       "
            "%s",
            idx,
            annotation.image_path,
            annotation.get_bounding_boxes(include_segmentations=True),
        )

        for bounding_box in annotation.get_bounding_boxes(include_segmentations=True):
            if annotation.is_valid_bounding_box(box=bounding_box.box):

                gt_bboxes.append(bounding_box.box.to_list(dst_type=float))

                gt_labels.append(bounding_box.class_id)
            else:
                logger.warning(
                    "Skip bounding-box because it doesn't fulfill "
                    "the requirements check by is_valid_bounding_box: \n"
                    "  - annotation.image_path: %s\n"
                    "  - bounding-box: %s",
                    annotation.image_path,
                    bounding_box,
                )

        if len(gt_bboxes) > 0:
            gt_bboxes_np = np.array(gt_bboxes, dtype=np.float32)
            gt_labels_np = np.array(gt_labels, dtype=np.int64)
        else:
            logger.warning(
                "No ground-truth bounding-boxes are given. "
                "Please remove this annotation from the csv: \n"
                "  - annotation.image_path: %s\n",
                annotation.image_path,
            )
            gt_bboxes_np = np.zeros((0, 4), dtype=np.float32)
            gt_labels_np = np.array([], dtype=np.int64)

        ann: Dict[str, Any] = dict(bboxes=gt_bboxes_np, labels=gt_labels_np)

        return ann
