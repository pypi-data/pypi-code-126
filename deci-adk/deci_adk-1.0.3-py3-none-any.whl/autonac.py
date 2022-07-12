import pickle
from importlib import util
from io import BytesIO
from typing import Any, Dict, List, Tuple, Union
from zipfile import ZipFile

from deci_lab_client.client import DeciPlatformClient  # type: ignore[import]
from deci_lab_client.models import AccuracyMetric, FrameworkType, Metric, OptimizationRequestForm, QuantizationLevel  # type: ignore[import]
from torch import nn, package


class UnknownPackagerError(Exception):
    def __init__(self, packager: str):
        super().__init__(f"Unknown packager '{packager}'. Please contact Deci support")


class UnknownModelError(Exception):
    def __init__(self, model_name: str):
        super().__init__(f"We couldn't find any model named {model_name} in your repository")


_RESOURCE_NAME = "model.pt"
_PICKLE_NAME = "model.nac"


class AutoNAC:
    def __init__(self, api_key: str, api_host: str = "api.deci.ai"):
        self.deci_api = DeciPlatformClient(api_host=api_host)
        self.deci_api.login(token=api_key)

    def add_model(
        self,
        new_name: str,
        base_model_name: str,
        model: nn.Module,
        quantization_level: QuantizationLevel = QuantizationLevel.FP16,
        accuracy_metric: List[AccuracyMetric] = [],
    ) -> None:
        model_metadata = self.deci_api.get_model_by_name(base_model_name).data
        model_metadata.name = new_name
        model_metadata.accuracy_metrics = accuracy_metric
        model_metadata.input_dimensions = []
        model_metadata.primary_hardware = model_metadata.primary_hardware.name
        model_metadata.error = None
        model_metadata.framework = FrameworkType.PYTORCH
        optimization_form = OptimizationRequestForm(
            target_hardware=model_metadata.primary_hardware,
            target_batch_size=model_metadata.primary_batch_size,
            target_metric=Metric.LATENCY,
            optimize_model_size=True,
            quantization_level=quantization_level,
            optimize_autonac=False,
        )
        self.deci_api.add_model(
            add_model_request=model_metadata, optimization_request=optimization_form, local_loaded_model=model
        )

    def get_model(
        self, model_name: str, pretrained_weights: bool = True
    ) -> Union[Tuple[nn.Module, Dict[str, Any]], nn.Module]:
        model = self.deci_api.get_model_by_name(model_name)

        if not model:
            raise UnknownModelError(model_name=model_name)

        file = self.deci_api.download_model(model.data.model_id).content

        loaded_file = AutoNAC._load_file(file)
        weights = loaded_file["weights"]
        packager = loaded_file["packager"]
        model = AutoNAC._get_package_content(file=file, packager=packager)

        recipe = None
        if util.find_spec("super_gradients") is not None:
            recipe = AutoNAC._get_package_content(
                file=file, packager=packager, package_name="additional_objects", resource="recipe"
            )
        else:
            print("Could not find 'super-gradients', not returning training recipe")

        del file
        if pretrained_weights and weights is not None:
            print("Loading weights from checkpoint file")
            model.load_state_dict(weights, strict=False)

        if recipe is not None:
            return model, recipe
        return model

    @classmethod
    def _get_package_content(
        cls, file: bytes, packager: str, package_name: str = "model", resource: str = _RESOURCE_NAME
    ) -> Any:
        if packager == "torch_package":
            with ZipFile(BytesIO(file)) as zipfile:
                imp = package.PackageImporter(BytesIO(zipfile.read(name=_RESOURCE_NAME)))
                return imp.load_pickle(package=package_name, resource=resource)
        raise UnknownPackagerError(packager=packager)

    @classmethod
    def _load_file(cls, file: bytes) -> Dict[str, Any]:
        io_bytes = BytesIO(file)
        with ZipFile(io_bytes) as zipfile:
            zipfile.extractall(
                members=[member for member in zipfile.namelist() if member not in [_PICKLE_NAME, _RESOURCE_NAME]]
            )
            return pickle.loads(zipfile.read(name=_PICKLE_NAME))
