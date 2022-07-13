import os
import base64
from io import BytesIO
import streamlit.components.v1 as components
from typing import Optional, Dict, Any, Sequence
from dataclasses import dataclass
from pathlib import Path

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


class ImageInputResult:
    def __init__(self, component_value: Dict[str, Any]) -> None:
        self._component_value = component_value

    def get_pil_image(self) -> Any:
        import PIL.Image # Make it an optional dependency
        return PIL.Image.open(BytesIO(base64.b64decode(self._component_value["b64"])))

    @property
    def origin(self) -> str:
        return self._component_value["origin"]

    @property
    def mime_type(self) -> str:
        return self._component_value["dataType"]


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
        initialDefaultPicture=initialDefaultPicture,
        maxPixels=maxPixels,
        presetImages=presetImages,
        key=key,
        default=None
    )
    if component_value is None:
        return None
    return ImageInputResult(component_value)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run template_component/__init__.py`
if __name__ == "__main__":
    import streamlit as st

    st.write("Select Image")
    result = image_input(
        initialDefaultPicture="https://source.unsplash.com/qDkso9nvCg0/600x799",
        presetImages=[
            "https://source.unsplash.com/2ShvY8Lf6l0/800x599",
            "https://source.unsplash.com/Dm-qxdynoEc/800x799",
            "https://source.unsplash.com/qDkso9nvCg0/600x799",
            "https://source.unsplash.com/iecJiKe_RNg/600x799",
            "https://source.unsplash.com/epcsn8Ed8kY/600x799",
            "https://source.unsplash.com/NQSWvyVRIJk/800x599",
            "https://source.unsplash.com/zh7GEuORbUw/600x799",
            "https://source.unsplash.com/PpOHJezOalU/800x599",
            "https://source.unsplash.com/I1ASdgphUH4/800x599",
            "https://source.unsplash.com/XiDA78wAZVw/600x799",
            "https://source.unsplash.com/x8xJpClTvR0/800x599",
            "https://source.unsplash.com/u9cG4cuJ6bU/4927x1000",
            "https://source.unsplash.com/qGQNmBE7mYw/800x599",
            "https://source.unsplash.com/NuO6iTBkHxE/800x599",
            "https://source.unsplash.com/pF1ug8ysTtY/600x400",
            "https://source.unsplash.com/A-fubu9QJxE/800x533",
            "https://source.unsplash.com/5P91SF0zNsI/740x494",
        ],
        key="123"
    )
    if result is None:
        st.write("No image selected")
    else:
        st.write(f"Image source: {result.origin}, type = {result.mime_type}")
        st.image(result.get_pil_image())
