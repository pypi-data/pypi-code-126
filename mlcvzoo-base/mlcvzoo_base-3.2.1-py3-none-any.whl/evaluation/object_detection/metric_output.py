# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Gathering of utility methods that are generating metric output in any
kind of form.
"""

import logging
from typing import Optional

import mlflow

from mlcvzoo_base.evaluation.object_detection.configuration import (
    TensorboardLoggingConfig,
)
from mlcvzoo_base.evaluation.object_detection.data_classes import (
    METRIC_DICT_TYPE,
    METRIC_IMAGE_INFO_TYPE,
)
from mlcvzoo_base.evaluation.object_detection.structs import BBoxSizeTypes

logger = logging.getLogger(__name__)


def log_od_metrics_to_mlflow(
    model_specifier: str,
    metrics_dict: METRIC_DICT_TYPE,
    iou_threshold: float,
    score_threshold: Optional[float] = None,
    nms_threshold: Optional[float] = None,
) -> None:
    """
    Log the object detection metrics for the given iou threshold with mlflow.
    This includes the logging of any metric that is defined by the
    dataclass mlcvzoo.evaluation.object_detection.data_classes.ODMetrics
    for any bounding box size type defined in the class
    mlcvzoo.evaluation.object_detection.structs.BBoxSizeTypes

    Args:
        model_specifier:
        metrics_dict: The metrics dictionary where to take the metrics from
        iou_threshold: The iou threshold for which the metrics should be logged
        score_threshold: Optionally hand over the score threshold with which the
                         metrics have been generated
        nms_threshold: Optionally hand over the nms threshold with which the
                      metrics have been generated

    Returns:
        None
    """

    if mlflow.active_run() is not None:
        logger.debug("Log mlflow metrics for model '%s'", model_specifier)

        if score_threshold is not None:
            mlflow.log_param(key="score_threshold", value=score_threshold)
        if nms_threshold is not None:
            mlflow.log_param(key="nms_threshold", value=nms_threshold)

        for bbox_size_type in BBoxSizeTypes.get_values_as_list(
            class_type=BBoxSizeTypes
        ):
            for class_name, od_metric in metrics_dict[iou_threshold][
                bbox_size_type
            ].items():
                mlflow.log_metric(
                    key=f"{class_name}_TP_{bbox_size_type}",
                    value=od_metric.TP,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_FP_{bbox_size_type}",
                    value=od_metric.FP,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_FN_{bbox_size_type}",
                    value=od_metric.FN,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_COUNT_{bbox_size_type}",
                    value=od_metric.COUNT,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_RC_{bbox_size_type}",
                    value=od_metric.RC,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_PR_{bbox_size_type}",
                    value=od_metric.PR,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_F1_{bbox_size_type}",
                    value=od_metric.F1,
                    step=0,
                )
                mlflow.log_metric(
                    key=f"{class_name}_AP_{bbox_size_type}",
                    value=od_metric.AP,
                    step=0,
                )
    else:
        logger.warning(
            "Can not log metrics with 'log_od_metrics_to_mlflow' for model '%s' "
            "since no mlflow run is active",
            model_specifier,
        )


def log_false_positive_info(
    model_specifier: str,
    metric_image_info_dict: METRIC_IMAGE_INFO_TYPE,
) -> None:
    """
    TODO

    Args:
        model_specifier:
        metric_image_info_dict:

    Returns:
        None
    """

    for class_name, image_dict in metric_image_info_dict.items():
        for image_path, metric_image_info in image_dict.items():
            if metric_image_info.false_positive_annotation is not None:
                bounding_boxes = (
                    metric_image_info.false_positive_annotation.get_bounding_boxes(
                        include_segmentations=True
                    )
                )

                logger.debug(
                    "\nFALSE POSITIVE for model %s: \n"
                    "  - image-path: '%s' \n"
                    "  - image-annotation: %s \n"
                    "  - bounding_boxes:   %s \n",
                    model_specifier,
                    metric_image_info.false_positive_annotation.image_path,
                    metric_image_info.false_positive_annotation.annotation_path,
                    bounding_boxes,
                )

            if metric_image_info.false_negative_annotation is not None:
                bounding_boxes = (
                    metric_image_info.false_negative_annotation.get_bounding_boxes(
                        include_segmentations=True
                    )
                )

                logger.debug(
                    "\nFALSE NEGATIVE for model %s: \n"
                    "  - image-path:       "
                    "%s\n"
                    "  - image-annotation: "
                    "%s\n"
                    "  - bounding_boxes:   %s\n",
                    model_specifier,
                    metric_image_info.false_negative_annotation.image_path,
                    metric_image_info.false_negative_annotation.annotation_path,
                    bounding_boxes,
                )


def log_false_positive_info_to_tb(
    model_name: str,
    metric_image_info_dict: METRIC_IMAGE_INFO_TYPE,
    tb_logging_config: TensorboardLoggingConfig,
) -> None:
    """
    Writes evaluation metrics and images to tensorboard directory.

    Args:
        model_name: TODO
        metric_image_info_dict: Dictionary mapping of string to a image dictionary
        tb_logging_config: configuration object defining the behavior of logging the
                           false positive information to tensorboard
        # TODO: Check how the size is determined (h+w or just w? what is the reference image?)

    Returns:
        None
    """

    # TODO: fix me

    # timestamp = datetime.now().strftime("%Y-%m-%dT_%H-%M")
    #
    # tb_dir = tb_logging_config.tensorboard_dir.replace(
    #     FileNamePlaceholders.TIMESTAMP, timestamp
    # )
    #
    # tb_dir = os.path.join(tb_dir, model_name)
    #
    # # NOTE: mypy error 'Call to untyped function "close" in typed context'
    # #       can be ignored
    # writer = SummaryWriter(tb_dir) if tb_dir != "" else SummaryWriter()  # type: ignore
    #
    # ensure_dir(file_path=tb_dir, verbose=True)
    #
    # logger.debug(
    #     "Write evaluation metrics/images to tensorboard-dir: '{}'".format(tb_dir)
    # )
    #
    # fn_color = (255, 0, 0)  # => black colour for ground truth boxes
    # fp_color = (0, 0, 0)  # => black colour for ground truth boxes
    # gt_color = (255, 255, 255)  # => white colour for false positives
    #
    # img_directory_id_dict: Dict[str, int] = dict()
    #
    # for class_name, image_dict in metric_image_info_dict.items():
    #     for image_path, metric_image_info in image_dict.items():
    #
    #         img = cv2.imread(image_path)
    #         img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #
    #         # resize to the configured image size
    #         height, width, _ = img.shape
    #
    #         if (
    #             metric_image_info.false_positive_annotation is not None
    #             or metric_image_info.false_negative_annotation is not None
    #         ) and metric_image_info.ground_truth_annotation is not None:
    #             __draw_annotation_on_tf_image(
    #                 img=img,
    #                 annotation=metric_image_info.ground_truth_annotation,
    #                 metric_type=MetricTypes.GROUND_TRUTH,
    #                 color=gt_color,
    #                 thickness=5,
    #             )
    #
    #         if metric_image_info.false_positive_annotation is not None:
    #             __draw_annotation_on_tf_image(
    #                 img=img,
    #                 annotation=metric_image_info.false_positive_annotation,
    #                 metric_type=MetricTypes.FALSE_POSITIVES,
    #                 color=fp_color,
    #                 thickness=2,
    #             )
    #
    #         if metric_image_info.false_negative_annotation is not None:
    #             __draw_annotation_on_tf_image(
    #                 img=img,
    #                 annotation=metric_image_info.false_negative_annotation,
    #                 metric_type=MetricTypes.FALSE_NEGATIVES,
    #                 color=fn_color,
    #                 thickness=2,
    #             )
    #
    #         # TODO: needed?
    #         # img_tensor = transforms.ToTensor()(img)
    #         #
    #         # scale_factor = tb_logging_config.false_positive_image_size / width
    #         #
    #         # img_tensor = functional.interpolate(
    #         #     img_tensor.unsqueeze(0),
    #         #     scale_factor=(scale_factor, scale_factor),
    #         #     mode="nearest",
    #         # ).squeeze(0)
    #         #
    #         # grid = torchvision.utils.make_grid(img_tensor)
    #
    #         if writer is not None:
    #             image_id, img_directory_id_dict = generate_img_id_map(
    #                 image_path=image_path, img_directory_id_dict=img_directory_id_dict
    #             )
    #
    #             if metric_image_info.ground_truth_annotation is not None:
    #                 gt_count = len(
    #                     metric_image_info.ground_truth_annotation.get_bounding_boxes(
    #                         include_segmentations=True
    #                     )
    #                 )
    #             else:
    #                 gt_count = 0
    #
    #             if metric_image_info.false_positive_annotation is not None:
    #                 fp_count = len(
    #                     metric_image_info.false_positive_annotation.get_bounding_boxes(
    #                         include_segmentations=True
    #                     )
    #                 )
    #             else:
    #                 fp_count = 0
    #
    #             if metric_image_info.false_negative_annotation is not None:
    #                 fn_count = len(
    #                     metric_image_info.false_negative_annotation.get_bounding_boxes(
    #                         include_segmentations=True
    #                     )
    #                 )
    #             else:
    #                 fn_count = 0
    #
    #             tf_string = (
    #                 f"{os.path.basename(image_path)}_"
    #                 f"ID_{image_id}_"
    #                 f"GT_{gt_count}_"
    #                 f"FP_{fp_count}_"
    #                 f"FN_{fn_count}"
    #             )
    #
    #             tensorboard_fp_image_path = (
    #                 f"metric_image_info_{class_name}/{tf_string}"
    #             )
    #
    #             # NOTE: mypy error 'Call to untyped function "close" in typed context'
    #             #       can be ignored
    #             writer.add_image(  # type: ignore
    #                 tag=tensorboard_fp_image_path,
    #                 img_tensor=img,
    #                 global_step=0,
    #             )
    #
    #         del img
    #
    # if writer is not None:
    #     # NOTE: mypy error 'Call to untyped function "close" in typed context' can be ignored
    #     writer.close()  # type: ignore
