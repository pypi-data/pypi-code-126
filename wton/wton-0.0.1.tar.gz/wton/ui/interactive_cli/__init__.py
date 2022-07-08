from json import JSONDecodeError

from pydantic import ValidationError
from .._utils import init_shared_object, setup_app
from wton.config import ConfigNotFoundError
from ._utils import echo_error
from ._sets import EntrypointSet


def main():
    try:
        context = init_shared_object()
        setup_app(context.config)

    except (FileNotFoundError, JSONDecodeError, ConfigNotFoundError, ValidationError) as e:
        echo_error(e)

    try:
        EntrypointSet(context).show()
    except KeyboardInterrupt:
        pass
