# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from os import PathLike
from functools import wraps
from typing import TypeVar, Callable, Any, Union, get_type_hints

from mldesigner._component_loader import _overwrite_component_load_options

_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])


def reference_component(path: Union[PathLike, str] = None, name=None, version=None, **kwargs) -> _TFunc:
    """Reference an existing component with a function and return a component node built with given params.
    The referenced component can be defined with local yaml file or in remote with name and version.
    The returned component node type are hint with function return annotation and default to Command.
    Eg: Both
    .. code-block:: python

        @reference_component()
        def my_func():
            ...
    and
    .. code-block:: python

        @reference_component()
        def my_func() -> Command:
            ...
    with return a Command node.
    .. code-block:: python

        @reference_component()
        def my_func() -> Parallel:
            ...
    will return a Parallel node.

    :param path: Path to local component file.
    :type path: str
    :param name: Name of component to load.
    :type name: str
    :param version: Version of component to load.
    :type version: str

    :return: Component node.
    :rtype: Union[Command, Parallel]
    """

    def component_decorator(func: _TFunc) -> _TFunc:
        @wraps(func)
        def wrapper(*args, **inner_kwargs):
            from azure.ai.ml import load_component
            from azure.ai.ml.entities._builders import Command, Parallel
            from azure.ai.ml.entities._job.pipeline._exceptions import UserErrorException

            if args:
                raise UserErrorException(
                    message="`reference_component` wrapped function only accept keyword parameters."
                )
            # call func to raise error when unknown kwargs are passed
            func(**inner_kwargs)

            if path:
                # load from local
                component = load_component(path=path)
            else:
                # load from remote
                # use function name as component name if not specified
                component_name = name or func.__name__

                component = component_name if version is None else f"{component_name}:{version}"

            component = _overwrite_component_load_options(func.__name__, component)

            result_cls = get_type_hints(func).get("return", Command)
            if issubclass(result_cls, Command):
                result_cls = Command
            elif issubclass(result_cls, Parallel):
                result_cls = Parallel
            else:
                allowed_cls = [Command, Parallel]
                msg = (
                    f"Return annotation of `reference_component` wrapped function can only be {allowed_cls} "
                    f"or it's subclass, got {result_cls} instead."
                )
                raise UserErrorException(message=msg)
            result = result_cls(component=component, inputs=inner_kwargs, _from_component_func=True)

            return result

        return wrapper

    return component_decorator
