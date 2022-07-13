import os
import base64
from typing import Optional
from dataclasses import dataclass
from pathlib import Path

from ..utils import declare_component


_component_func = declare_component(Path(__file__).absolute())


@dataclass
class AudioInputComponentOutput:
    data: bytes
    mime_type: str

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def audio_input(key=None) -> Optional[AudioInputComponentOutput]:
    """TODO: DOC
    """

    component_data = _component_func(key=key, default=None)
    if component_data is None:
        return None
    message_bytes = component_data['b64'].encode('ascii')
    base64_bytes = base64.b64decode(message_bytes)
    return AudioInputComponentOutput(
        data=base64_bytes,
        mime_type=component_data['mime_type']
    )
