# Encoding: UTF-8
# pylint: disable=missing-module-docstring

from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Final,
    Generic,
    Hashable,
    Optional,
    TypeVar,
    Union,
)

S = TypeVar("S")
_NONE: Final = type


class MissingCallbackError(Exception):
    pass


class Store:
    """Globally store the state of a value."""

    store: dict[Hashable, Any] = {}

    @classmethod
    def __init__(cls, key: Hashable, value: Any) -> None:
        """# TODO: Documentation."""
        cls.store.update({key: value})

    @classmethod
    def set(cls, key: Hashable, value: Any) -> None:
        """# TODO: Documentation."""
        cls.store.update({key: value})

    @classmethod
    def get(cls, key: Hashable):
        """# TODO: Documentation."""
        return cls.store[key]

    @classmethod
    def delete(cls, key: Hashable) -> None:
        """# TODO: Documentation."""
        del cls.store[key]


@dataclass
class State(Generic[S]):
    """Locally stores state."""

    state: S

    def __call__(self, state: Union[S, _NONE] = _NONE):
        if state is _NONE:
            return self.state

        self.state = state
        return None

    def get(self):
        """Get the current state."""
        return self.state

    def set(self, state: S) -> None:
        """Set the current state."""
        self.state = state


@dataclass
class Derive(Generic[S]):
    """Derive from a state's value."""

    state: State
    callback: Optional[Callable[[Any], Any]] = None

    def __call__(self):
        if isinstance(self.callback, Callable):
            self.callback(self.state())

        return self.state()

    def get_callback(self):
        """# TODO: Documentation."""
        if isinstance(self.callback, Callable):
            return self.callback(self.state())

        raise MissingCallbackError("No callback provided")


__all__ = ("State", "Derive", "Store")
