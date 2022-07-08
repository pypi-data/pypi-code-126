import logging
from logging.handlers import RotatingFileHandler
from typing import Union


def start_logger(level: Union[int, str] = logging.INFO) -> logging.Logger:
    """Initializes a RotatingFileHanlder and a StreamHandler for logging.
    This function creates a logger with two handlers (RotatingFileHandler and StreamHandler) that can come in handy, if
    no other logging handlers are being used. The RotatingFileHandler writes it's output to 'oopnet.log' and rotates the
    file when it reaches a size of 5 MB.
    Args:
        level: logging level (e.g., logging.DEBUG)
    Returns:
        logger object
    """
    logger = logging.getLogger("oopnet")
    logger.setLevel(level)
    format = logging.Formatter("%(asctime)s:  %(name)s - %(levelname)s - %(message)s")
    f_handler = RotatingFileHandler("sfc.log", maxBytes=5_000_000)
    f_handler.setFormatter(format)
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(format)
    logger.addHandler(f_handler)
    logger.addHandler(logging.StreamHandler())
    return logger
