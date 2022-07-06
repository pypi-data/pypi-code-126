import functools
import inspect
import logging
import sys
import timeit


def log_timing(fn):
    qualified_name = get_qualified_name(fn)

    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        start = timeit.default_timer()
        ret = fn(*args, **kwargs)
        end = timeit.default_timer()
        logger = logging.getLogger(fn.__module__)
        logger.info(
            "'%s' from '%s' took %0.3f ms",
            qualified_name,
            fn.__module__,
            (end - start) * 1000,
            extra={"category": "perf"},
        )
        return ret

    return wrapped


def get_qualified_name(func):
    if sys.version_info >= (3, 3):
        result = func.__qualname__
    else:
        if is_method(func):
            result = ".".join([func.__class__.__name__, func.__name__])
        else:
            result = func.__name__
    return result


def is_method(func):
    try:
        # Get the name and default values of function's parameters if to see if it is a method.
        # Used instead of inspect.ismethod() and similar functions because decorators
        # are applied before class is created, so all methods are in fact functions at time when decorator is applied
        if sys.version_info >= (3, 0):
            result = inspect.getfullargspec(func)[0][0] == "self"
        else:
            result = inspect.getargspec(func)[0][0] == "self"
    except LookupError:
        result = False

    return result
