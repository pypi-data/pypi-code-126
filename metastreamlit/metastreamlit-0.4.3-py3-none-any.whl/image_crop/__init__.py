import os
import base64
from io import BytesIO
from pathlib import Path
import streamlit.components.v1 as components
from typing import Optional, Any, Dict

from ..utils import image_to_url, declare_component


_component_func = declare_component(Path(__file__).absolute())


class ImageCropResult:
    def __init__(self, input_image: Any, component_value: Dict[str, Any]) -> None:
        self._component_value = component_value
        self._input_image = input_image

    @property
    def x(self) -> int:
        return int(self._component_value["x"])
    @property
    def y(self) -> int:
        return int(self._component_value["y"])
    @property
    def width(self) -> int:
        return int(self._component_value["width"])
    @property
    def height(self) -> int:
        return int(self._component_value["height"])


def image_crop(image: Any, previewResult: bool = False, key=None) -> Optional[ImageCropResult]:
    """Create a new instance of "my_component".

    Parameters
    ----------
    image: str or PIL.Image
        The image to crop. Can be either a URL or a PIL.Image
    previewResult: bool
        If the component should also render the selected crop
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    ImageCropResult or None

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(image=image_to_url(image), previewResult=previewResult, key=key, default=None)
    if component_value is None:
        return None
    return ImageCropResult(image, component_value)
