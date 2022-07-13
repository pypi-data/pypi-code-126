import logging

FORMAT = '%(asctime)-1s - %(name)s - [%(levelname)s]:: %(message)s'


def init_logging(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(FORMAT)
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger
