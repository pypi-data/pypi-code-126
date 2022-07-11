import logging
import os
from typing import Dict, List, Optional

from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.model import ObjectDetectionModel
from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.configuration.structs import MLFlowExperimentTypes
from mlcvzoo_base.evaluation.object_detection.data_classes import (
    ODModelEvaluationMetrics,
)
from mlcvzoo_base.evaluation.object_detection.object_detection_evaluator import (
    ObjectDetectionEvaluator,
)
from mlcvzoo_base.metrics.mlflow.mlflow_runner import MLFLowRunner
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils import get_project_path_information


def evaluate_all_models(
    evaluator: ObjectDetectionEvaluator,
    model_configs: List[ModelConfig],
    string_replacement_map: Optional[Dict[str, str]] = None,
    gt_annotations: Optional[List[BaseAnnotation]] = None,
) -> List[ODModelEvaluationMetrics]:
    """
    Run an evaluation on all models that are defined in the model_configs of the
    ODEvaluationConfig configuration. The evaluation is performed on the basis of the
    given ground truth annotations or otherwise on the basis of the ground truth annotations
    that can be parsed via the annotation handler configuration from the ODEvaluationConfig
    of this instance.

    Args:
        evaluator: evaluator instance for running the evaluation
        model_configs: configurations for model which should be evaluated
        string_replacement_map: A dictionary that defines placeholders which can be used
                                while parsing the file. They can be understood as variables
                                that can be used to define configs that are valid across
                                multiple devices.
        gt_annotations: Optionally hand over ground truth annotations where the model should
                        be evaluated on

    Returns:
        A list containing the computed metrics of every model
    """

    model_registry = ModelRegistry()

    models_metrics_list: List[ODModelEvaluationMetrics] = []

    for model_config in model_configs:

        model: Model[PredictionType, ConfigurationType, DataType]  # type: ignore
        model = model_registry.init_model(
            model_config=model_config,
            string_replacement_map=string_replacement_map,
        )

        if not isinstance(model, ObjectDetectionModel):
            raise ValueError(
                "This evaluation can only be used with models that "
                "inherit from 'mlcvzoo.api.model.ObjectDetectionModel'"
            )

        models_metrics_list.append(
            evaluator.evaluate_with_model(model=model, gt_annotations=gt_annotations)
        )

    return models_metrics_list


# TODO: Currently this can only perform object detection, extend to other evaluation types
def main() -> None:

    _, project_root, _ = get_project_path_information(
        file_path=__file__, dir_depth=3, code_base="mlcvzoo_base"
    )

    Logger.init_logging_basic(
        log_dir=os.path.join(project_root, "logs"),
        log_file_postfix="ObjectDetectionEvaluator",
        no_stdout=False,
        root_log_level=logging.DEBUG,
        file_log_level=logging.DEBUG,
        stdout_log_level=logging.INFO,
    )

    evaluator = ObjectDetectionEvaluator()

    mlflow_runner: Optional[MLFLowRunner] = None
    if evaluator.config.mlflow_config is not None:
        mlflow_runner = MLFLowRunner(
            configuration=evaluator.config.mlflow_config,
        )

    if evaluator.config.model_configs is None:
        raise ValueError(
            "Please add model_configs to the ObjectDetectionEvaluator configuration file,"
            "in order to run the ObjectDetectionEvaluator tool."
        )

    models_metric_list = evaluate_all_models(
        evaluator=evaluator,
        model_configs=evaluator.config.model_configs,
        string_replacement_map=None,
        gt_annotations=None,
    )

    for model_metrics in models_metric_list:
        if mlflow_runner is not None:
            mlflow_runner.start_mlflow_run(
                experiment_name=MLFlowExperimentTypes.EVAL,
                run_name=model_metrics.model_specifier,
                end_runs_in_advance=True,
            )

        evaluator.output_evaluation_results(model_metrics=model_metrics)

        if mlflow_runner is not None:
            mlflow_runner.end_run()


if __name__ == "__main__":
    main()
