# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging


class _LoggerFactory:
    @staticmethod
    def get_logger(name="mldesigner", verbosity=logging.INFO):
        logger = logging.getLogger(name)
        logger.propagate = False
        logger.setLevel(logging.DEBUG)
        if not _LoggerFactory._find_handler(logger, logging.StreamHandler):
            # Expose mldesigner log to terminal.
            handler = logging.StreamHandler()
            formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s] - %(message)s")
            handler.setFormatter(formatter)
            handler.setLevel(verbosity)
            logger.addHandler(handler)
        return logger

    @staticmethod
    def _find_handler(logger, handler_type):
        for log_handler in logger.handlers:
            if isinstance(log_handler, handler_type):
                return log_handler
        return None
