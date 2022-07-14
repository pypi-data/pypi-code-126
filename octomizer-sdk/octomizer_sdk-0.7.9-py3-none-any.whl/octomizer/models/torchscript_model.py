"""A wrapper for Torchscript Models in the OctoML Platform."""
import typing

from octomizer import client, model, project


class TorchscriptModel(model.Model):
    """Represents a Model in Torchscript format."""

    def __init__(
        self,
        client: client.OctomizerClient,
        name: str,
        model: typing.Optional[typing.Union[bytes, str]] = None,
        model_input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        model_input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.List[str]] = None,
        project: typing.Optional[project.Project] = None,
        timeout: int = model.DEFAULT_JOB_TIMEOUT_SECONDS,
    ):
        """Creates a new Torchscript model in the OctoML Platform.

        :param client: an instance of the OctoML client.
        :param name: the name of the model.
        :param model: The model bytes, or the name of a file containing the Torchscript model.
        :param model_input_shapes: The model's input shapes in key, value format. e.g. {"input0": [1, 3, 224, 224]}.
        :param model_input_dtypes: The model's input dtypes in key, value format. e.g. {"input0": "float32"}
        :param description: a description of the model.
        :param labels: optional tags for the Model.
        :param project: the Project that this Model belongs to. Optional.
        """
        super().__init__(
            client=client,
            name=name,
            model=model,
            model_input_shapes=model_input_shapes,
            model_input_dtypes=model_input_dtypes,
            description=description,
            labels=labels,
            model_format="torchscript",
            project=project,
            timeout=timeout,
        )
