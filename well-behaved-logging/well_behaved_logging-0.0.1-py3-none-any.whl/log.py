import logging
from logging import Handler, StreamHandler, NullHandler
import sys
from typing import List, Optional, Union


__all__ = ["getLogger", "start_logging", "stop_logging"]


def _ensure_handler(name):
    top = name.split(".", 1)[0]
    logger = logging.getLogger(top)

    if len(logger.handlers) == 0:
        logger.addHandler(NullHandler())


def getLogger():
    """
    Get well-bahaved Logger

    This function doesn't set any log level nor handlers to the module-level logger.
    However, it ensures that the package top-level logger (not root logger) has
    at least one logger.

    Returns
    -------
    logging.Logger
        Module-level ``Logger``.
    """
    frame = list(sys._current_frames().values())[0]
    name = frame.f_back.f_globals.get("__name__", None)
    logger = logging.getLogger(name)

    _ensure_handler(name)

    return logger


def start_logging(name: str,
                  level: Optional[int] = None, *,
                  handlers: Optional[Union[Handler, List[Handler]]] = None,
                  propagate: bool = False):
    """
    Start logging

    Parameters
    ----------
    name : str
        Module or package name to be logged.
    level : int, optional
        Log level. If ``None`` (default), ``logging.DEBUG`` is used.
    handlers : Handler or list of Handler, optional
        Handlers to be used for logging. If ``None`` (default),
        ``StreamHandler`` is used.
    propagate : bool, optional
        Whether logs of this module are passed to its parent logger.
        The default is ``False``
    """
    logger = logging.getLogger(name)

    if level is None:
        level = logging.DEBUG

    if handlers is None:
        handlers = [StreamHandler()]
    elif isinstance(handlers, Handler):
        handlers = [handlers]

    if len(logger.handlers) == 1 and isinstance(logger.handlers[0], NullHandler):
        logger.removeHandler(logger.handlers[0])

    for h in handlers:
        logger.addHandler(h)

    logger.setLevel(level)
    logger.propagate = propagate


def stop_logging(name: str):
    """
    Stop logging

    Parameters
    ----------
    name : str
        Module or package name to stop logging.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.NOTSET)

    for h in [h for h in logger.handlers]:
        if isinstance(h, StreamHandler):
            h.flush()
        logger.removeHandler(h)

    logger.propagate = True
    _ensure_handler(name)
