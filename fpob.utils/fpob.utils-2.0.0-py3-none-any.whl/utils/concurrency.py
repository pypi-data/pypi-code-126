import functools
import threading
import typing as t


F = t.TypeVar('F', bound=t.Callable[..., t.Any])


def atomic(fn: F) -> F:
    """
    Decorator to prevent prevent multiple threads from executing the function
    simultaneously. Achieved by wrapping the call into ``threading.RLock``.
    """
    lock = threading.RLock()

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        with lock:
            return fn(*args, **kwargs)

    return t.cast(F, inner)
