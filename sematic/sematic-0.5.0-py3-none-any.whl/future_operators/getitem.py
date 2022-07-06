"""
Defining these operators in seperate modules in order to avoid circular
dependencies between Future and Calculator
"""
# Standard library
from types import GenericAlias
from typing import Any, cast

# Sematic
from sematic.future import Future
from sematic.types.casting import can_cast_type, safe_cast
from sematic.calculator import func


def __getitem__(self: Future, key: Any):
    """
    Implementation of __getitem__ on Futures.

    When users try to access an item on a future returning a list, tuple, dict,
    a new Sematic Function needs to be created on the fly to access the item.
    """
    future_type: GenericAlias = cast(GenericAlias, self.calculator.output_type)

    try:
        origin_type = future_type.__origin__
    except AttributeError:
        raise TypeError("__getitem__ is not supported on type {}".format(future_type))

    if origin_type not in (tuple, list, dict):
        raise TypeError("__getitem__ is not supported on type {}".format(future_type))

    element_types = future_type.__args__

    if origin_type is dict:
        key_type, value_type = element_types

        if isinstance(key, Future):
            _, error = can_cast_type(key.calculator.output_type, key_type)
        else:
            _, error = safe_cast(key, key_type)

        if error is not None:
            raise TypeError("Invalid key {}: {}".format(repr(key), error))

    if origin_type is tuple:
        key_type = int
        value_type = element_types[key]

    if origin_type is list:
        key_type = int
        value_type = element_types[0]

    @func
    def _getitem(container: future_type, key: key_type) -> value_type:  # type: ignore
        return container[key]  # type: ignore

    return _getitem(self, key)


Future.__getitem__ = __getitem__  # type: ignore
