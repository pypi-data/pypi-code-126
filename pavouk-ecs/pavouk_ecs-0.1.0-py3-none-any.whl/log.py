import logging


_loggers = {}


def getLogger(name):
    if name not in _loggers:
        _loggers[name] = _create_logger(name)

    return _loggers[name]


def _create_logger(name):
    logger = logging.getLogger(name)
    # logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(name)s %(message)s - %(funcName)s '
        '%(pathname)s:%(lineno)d')

    file_handler = logging.FileHandler('pavouk-ecs.log')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)

    return logger


def disable_loggers():
    for i in _loggers:
        _loggers[i].disabled = True
