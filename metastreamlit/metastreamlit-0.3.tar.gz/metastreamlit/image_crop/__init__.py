import os
import base64
from io import BytesIO
from pathlib import Path
import streamlit.components.v1 as components
from typing import Optional, Any, Dict

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = (__name__ != "__main__")

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

_COMPONENT_NAME = Path(__file__).absolute().parent.name

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        _COMPONENT_NAME,
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "build")
    _component_func = components.declare_component(_COMPONENT_NAME, path=build_dir)


def _image_to_url(image: Any) -> str:
    # URL
    if isinstance(image, str):
        return image
    # Pillow image
    import PIL.Image
    if isinstance(image, PIL.Image.Image):
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        r = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
        r = r.decode("utf-8")
        return r
    raise RuntimeError(f"Unsupported image type: {type(image)}. Provide a string (URL) or a PIL.Image")


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
    component_value = _component_func(image=_image_to_url(image), previewResult=previewResult, key=key, default=None)
    if component_value is None:
        return None
    return ImageCropResult(image, component_value)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run template_component/__init__.py`
if __name__ == "__main__":
    import streamlit as st
    import PIL.Image
    import numpy as np

    st.header("With image=URL")
    crop = image_crop(image="https://source.unsplash.com/qDkso9nvCg0/600x799", key='url')
    if crop is not None:
        st.write(f"Crop pos: ({crop.x}, {crop.y}) - width={crop.width}, height={crop.height}")

    st.header("With image=PIL.Image")
    np.random.seed(0)
    random_array = np.random.randint(low=0, high=255, size=(250,250), dtype=np.uint8)
    random_im = PIL.Image.fromarray(random_array)
    crop = image_crop(image=random_im, key='pil')
    if crop is not None:
        st.write(f"Crop pos: ({crop.x}, {crop.y}) - width={crop.width}, height={crop.height}")
