# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for running an evaluation for object detection models
"""

import logging
import typing
from typing import Dict, List, Optional

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
from mlcvzoo_base.data_preparation.AnnotationHandler import AnnotationHandler
from mlcvzoo_base.evaluation.object_detection.configuration import ODEvaluationConfig
from mlcvzoo_base.evaluation.object_detection.data_classes import (
    EVALUATION_LIST_TYPE,
    ODModelEvaluationMetrics,
)
from mlcvzoo_base.evaluation.object_detection.metric_output import (
    log_false_positive_info,
    log_false_positive_info_to_tb,
    log_od_metrics_to_mlflow,
)
from mlcvzoo_base.evaluation.object_detection.metrics_evaluation import (
    MetricsEvaluation,
)
from mlcvzoo_base.evaluation.object_detection.utils import generate_metric_table

logger = logging.getLogger(__name__)


class ObjectDetectionEvaluator(ConfigBuilder):
    """
    TODO
    """

    def __init__(
        self,
        configuration: Optional[ODEvaluationConfig] = None,
        yaml_config_path: Optional[str] = None,
        mutual_attribute_map: Optional[Dict[str, List[str]]] = None,
        no_checks: bool = False,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> None:

        ConfigBuilder.__init__(
            self,
            class_type=ODEvaluationConfig,
            configuration=configuration,
            yaml_config_path=yaml_config_path,
            argparse_module_description="Run evaluation for Object-Detection models.",
            mutual_attribute_map=mutual_attribute_map,
            no_checks=no_checks,
            string_replacement_map=string_replacement_map,
        )

        self.config: ODEvaluationConfig = typing.cast(
            ODEvaluationConfig, self.configuration
        )

        self.models: Optional[List[Model[PredictionType, ConfigurationType, DataType]]]  # type: ignore
        self.models = None
        self.annotation_handler: Optional[AnnotationHandler] = None
        self.gt_annotations: List[BaseAnnotation] = []

        self.all_predicted_annotations: EVALUATION_LIST_TYPE = []
        self.all_gt_annotations: EVALUATION_LIST_TYPE = []

    def __init_gt_annotations(
        self, gt_annotations: Optional[List[BaseAnnotation]] = None
    ) -> None:

        if gt_annotations is not None:
            self.gt_annotations = gt_annotations
        else:
            assert self.config.annotation_handler_config is not None
            assert self.config.input_data is not None

            self.annotation_handler = AnnotationHandler(
                configuration=self.config.annotation_handler_config,
            )

            self.gt_annotations = []

            for input_data in self.config.input_data:
                self.gt_annotations.extend(
                    self.annotation_handler.parse_annotations_from_csv(
                        csv_file_path=input_data.csv_file_path
                    )
                )

    @staticmethod
    def __compute_metrics_with_precomputed_data(
        metrics_evaluation: MetricsEvaluation,
        ground_truth_annotations: List[BaseAnnotation],
        predicted_bounding_boxes_list: List[List[BoundingBox]],
    ) -> None:

        """
        Fill out basic evaluation lists which are needed to compute the metrics.

        Use already gather ground-truth annotations and predicted bounding boxes.
        Both lists have to be of the same size. A single item of the lists stands
        for an image index.
        """

        process_bar = tqdm(
            zip(ground_truth_annotations, predicted_bounding_boxes_list),
            desc=f"Compute metrics: ",
        )

        # TODO: replace by batch-processing? Or data-stream?
        for index, (gt_annotation, predicted_bounding_boxes) in enumerate(process_bar):

            _ = metrics_evaluation.update_from_prediction(
                index=index,
                gt_annotation=gt_annotation,
                predicted_bounding_boxes=predicted_bounding_boxes,
            )

    def __compute_metrics_model_based(
        self,
        metrics_evaluation: MetricsEvaluation,
        model: ObjectDetectionModel[ConfigurationType, DataType],
    ) -> None:
        """
        Fill out basic evaluation lists which are needed to compute the metrics.

        Use a model to predict results on the images given via the annotation-handler configuration
        """

        assert isinstance(model, ObjectDetectionModel)

        process_bar = tqdm(self.gt_annotations, desc=f"Compute metrics: ")

        # TODO: replace by batch-processing? Or data-stream?
        for index, gt_annotation in enumerate(process_bar):

            # BoundingBox is defined for API usages. All model implementations return the
            # sub-class BoundingBox
            _, predicted_bounding_boxes = model.predict(
                data_item=gt_annotation.image_path
            )

            _ = metrics_evaluation.update_from_prediction(
                index=index,
                gt_annotation=gt_annotation,
                predicted_bounding_boxes=predicted_bounding_boxes,
            )

    def evaluate_with_model(
        self,
        model: ObjectDetectionModel[ConfigurationType, DataType],
        gt_annotations: Optional[List[BaseAnnotation]] = None,
    ) -> ODModelEvaluationMetrics:
        """
        Compute the metric for the given object detection model. The evaluation is performed
        on the basis of the given ground truth annotations or otherwise on the basis of the
        ground truth annotations that can be parsed via the annotation handler configuration
        from the ODEvaluationConfig of this instance.

        Args:
            model: The model that should be evaluated
            gt_annotations: Optionally hand over ground truth annotations where the model should
                            be evaluated on

        Returns:
            The computed object detection metrics for this model
        """

        self.__init_gt_annotations(gt_annotations=gt_annotations)

        metrics_evaluation = MetricsEvaluation(
            model_specifier=model.get_name(),
            classes_id_dict=model.get_classes_id_dict(),
            iou_thresholds=self.config.iou_thresholds,
            dataset_length=len(self.gt_annotations),
        )

        self.__compute_metrics_model_based(
            metrics_evaluation=metrics_evaluation,
            model=model,
        )

        return metrics_evaluation.compute_metrics()

    def evaluate_with_precomputed_data(
        self,
        model_specifier: str,
        classes_id_dict: Dict[int, str],
        ground_truth_annotations: List[BaseAnnotation],
        predicted_bounding_boxes_list: List[List[BoundingBox]],
    ) -> ODModelEvaluationMetrics:
        """
        Compute the object detection metrics taking precomputed (predicted) bounding boxes and
        ground truth annotations.

        IMPORTANT REMARK: The index of the lists 'ground_truth_annotations'
                          and 'predicted_bounding_boxes_list' have to match exactly. This means
                          index 0 indicates the ground truth data and predicted bounding boxes
                          for image 0.

        Args:
            model_specifier: A string to indicate with which model the precomputed bounding boxes
                             have been predicted
            classes_id_dict: A dictionary that defines the mapping of class ids to class names for
                             this evaluation
            ground_truth_annotations: The ground truth data as basis for the evaluation
            predicted_bounding_boxes_list: The bounding boxes that have been predicted by a model

        Returns:
            The computed object detection metrics
        """

        assert len(ground_truth_annotations) == len(predicted_bounding_boxes_list)

        metrics_evaluation = MetricsEvaluation(
            model_specifier=model_specifier,
            classes_id_dict=classes_id_dict,
            iou_thresholds=self.config.iou_thresholds,
            dataset_length=len(ground_truth_annotations),
        )

        self.__compute_metrics_with_precomputed_data(
            metrics_evaluation=metrics_evaluation,
            ground_truth_annotations=ground_truth_annotations,
            predicted_bounding_boxes_list=predicted_bounding_boxes_list,
        )

        return metrics_evaluation.compute_metrics()

    def output_evaluation_results(
        self,
        model_metrics: ODModelEvaluationMetrics,
        score_threshold: Optional[float] = None,
        nms_threshold: Optional[float] = None,
    ) -> None:
        """
        Generate logging output.
        - python logging
        - log object detection metrics to mlflow
        - visualize information about false positives and false negatives by logging
          images to tensorboard

        Args:
            model_metrics: An ODModelEvaluationMetrics object storing the information of an
                           evaluation computation
            score_threshold: Optionally hand over the score threshold, indicating the score
                             threshold that has been used to filter predicted bounding boxes
            nms_threshold: Optionally hand over the nms threshold, indicating the nms
                           threshold that has been used to filter predicted bounding boxes

        Returns:
            None
        """

        for iou_threshold in self.config.iou_thresholds:
            metric_table = generate_metric_table(
                metrics_dict=model_metrics.metrics_dict,
                iou_threshold=iou_threshold,
            )

            score_string = (
                f"{score_threshold:.2f}" if score_threshold is not None else "NONE"
            )
            nms_string = f"{nms_threshold:.2f}" if nms_threshold is not None else "NONE"

            logger.info(
                "\n\n"
                " Evaluation result for "
                "model '%s', "
                "IOU= %.2f, "
                "SCORE= %s, "
                "NMS= %s: \n"
                "%s"
                "\n\n",
                model_metrics.model_specifier,
                iou_threshold,
                score_string,
                nms_string,
                metric_table.table,
            )

            log_od_metrics_to_mlflow(
                model_specifier=model_metrics.model_specifier,
                metrics_dict=model_metrics.metrics_dict,
                score_threshold=score_threshold,
                nms_threshold=nms_threshold,
                iou_threshold=iou_threshold,
            )

        log_false_positive_info(
            model_specifier=model_metrics.model_specifier,
            metric_image_info_dict=model_metrics.metrics_image_info_dict,
        )

        if self.config.tensorboard_logging is not None:
            log_false_positive_info_to_tb(
                model_name=model_metrics.model_specifier,
                metric_image_info_dict=model_metrics.metrics_image_info_dict,
                tb_logging_config=self.config.tensorboard_logging,
            )
