import os
import base64
from io import BytesIO
import streamlit.components.v1 as components
from typing import Optional, Dict, Any, Sequence
from dataclasses import dataclass
from pathlib import Path

from ..utils import image_to_url, declare_component


_component_func = declare_component(Path(__file__).absolute())


class ImageInputResult:
    def __init__(self, *, component_value: Optional[Dict[str, Any]] = None, input_pil_image = None) -> None:
        self._component_value = component_value
        self._input_pil_image = input_pil_image

    def get_pil_image(self) -> Any:
        import PIL.Image # Make it an optional dependency
        if self._component_value is None:
            return self._input_pil_image
        return PIL.Image.open(BytesIO(base64.b64decode(self._component_value["b64"])))

    @property
    def origin(self) -> str:
        if self._component_value is None:
            return "default"
        return self._component_value["origin"]


def image_input(initialDefaultPicture: Optional[str] = None, maxPixels: int = 512 * 512, presetImages: Optional[Sequence[str]] = None, key=None) -> Optional[ImageInputResult]:
    """Create a new instance of "my_component".

    Parameters
    ----------
    initialDefaultPictureURL: str or None
        URL of the initially selected picture
    maxPixels: int
        Maximum number of pixels in the uploaded image. Will be down-scaled if necessary
    presetImages: List of str or NOne
        A list of preset images to choose from
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(
        initialDefaultPicture=image_to_url(initialDefaultPicture),
        maxPixels=maxPixels,
        presetImages=[image_to_url(i) for i in presetImages] if presetImages is not None else [],
        key=key,
        default=None
    )
    if component_value is None:
        if not isinstance(initialDefaultPicture, str):
            return ImageInputResult(input_pil_image=initialDefaultPicture)
        return None
    return ImageInputResult(component_value=component_value)
