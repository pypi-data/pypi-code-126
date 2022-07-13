from io import BytesIO
import base64
import os
from typing import Any
from pathlib import Path
from threading import Lock
import streamlit.components.v1 as components


def image_to_url(image: Any) -> str:
    # URL
    if isinstance(image, str):
        return image
    # Pillow image
    import PIL.Image
    if isinstance(image, PIL.Image.Image):
        buffered = BytesIO()
        image.convert("RGB").save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        r = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
        return r.decode("utf-8")
    raise RuntimeError(f"Unsupported image type: {type(image)}. Provide a string (URL) or a PIL.Image")


def declare_component(path: Path):
    # Declare a Streamlit component. `declare_component` returns a function
    # that is used to create instances of the component. We're naming this
    # function "_component_func", with an underscore prefix, because we don't want
    # to expose it directly to users. Instead, we will create a custom wrapper
    # function, below, that will serve as our component's public API.

    # It's worth noting that this call to `declare_component` is the
    # *only thing* you need to do to create the binding between Streamlit and
    # your component frontend. Everything else we do in this file is simply a
    # best practice.

    component_name = path.parent.name
    serve_url = os.environ.get(f"{component_name.upper()}_URL", None)
    print("serve_url", f"{component_name.upper()}_URL", serve_url)


    if serve_url is not None:
        return components.declare_component(
            # We give the component a simple, descriptive name ("my_component"
            # does not fit this bill, so please choose something better for your
            # own component :)
            component_name,
            # Pass `url` here to tell Streamlit that the component will be served
            # by the local dev server that you run via `npm run start`.
            # (This is useful while your component is in development.)
            url=serve_url,
        )
    else:
        # When we're distributing a production version of the component, we'll
        # replace the `url` param with `path`, and point it to to the component's
        # build directory:
        build_dir = str(path.parent / "build")
        return components.declare_component(component_name, path=build_dir)


def _get_global_object(name, default_ctor):
    from matplotlib.backends.backend_agg import RendererAgg
    import sys
    GLOBAL_CONTAINER = sys

    if not hasattr(GLOBAL_CONTAINER, '_global_state'):
        with RendererAgg.lock:
            if not hasattr(GLOBAL_CONTAINER, '_global_state'):
                GLOBAL_CONTAINER._global_state = {}
                GLOBAL_CONTAINER._global_lock = Lock()

    if name not in GLOBAL_CONTAINER._global_state:
        with GLOBAL_CONTAINER._global_lock:
            if name not in GLOBAL_CONTAINER._global_state:
                GLOBAL_CONTAINER._global_state[name] = default_ctor()

    return GLOBAL_CONTAINER._global_state[name]


def critical_section(name: str):
    lock = _get_global_object(f"{name}.lock", Lock)
    def make_locked(func):
        def inner(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return inner
    return make_locked
