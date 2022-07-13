""" 
Python logging module wrapper for
- GELF format
- syslog level
+----------------------+------------------------+------------------------+
| Level name           | Severity value         | Logger method          |
+======================+========================+========================+
| ``EMERGENCY``        | 0                      | |logger.emerg|         |
+----------------------+------------------------+------------------------+
| ``ALERT``            | 1                      | |logger.alert|         |
+----------------------+------------------------+------------------------+
| ``CRITICAL``         | 2                      | |logger.crit|          |
+----------------------+------------------------+------------------------+
| ``ERROR``            | 3                      | |logger.err|           |
+----------------------+------------------------+------------------------+
| ``WARNING``          | 4                      | |logger.warning|       |
+----------------------+------------------------+------------------------+
| ``NOTICE``           | 5                      | |logger.notice|        |
+----------------------+------------------------+------------------------+
| ``INFO``             | 6                      | |logger.info|          |
+----------------------+------------------------+------------------------+
| ``DEBUG``            | 7                      | |logger.debug|         |
+----------------------+------------------------+------------------------+

# Usages:

logging examples:

logger.debug("test")
logger.debug("test", {"project_id": 2567})


Set log threshold:
logger.set_level("INFO")

"""


import logging
import json
import socket
import sys
from enum import IntEnum
from typing import Union

#====== Definitions ======

GELF_VERSION = "1.1" 
""" 
GELF deafult version
TODO: allow config?
"""

#===== [ Log Level Definition ] =====
_nameToLevel = {
    "EMERGENCY" : 0,
    "ALERT" : 1,
    "CRITICAL" : 2,
    "ERROR" : 3,
    "WARNING" : 4,
    "NOTICE" : 5,
    "INFO" : 6,
    "DEBUG" : 7
}
""" syslog level map string to int """


class LOG_LEVEL(IntEnum):
    """
    abstract log level for python log level
    for python logging: higher level = higher serverity
    keep this hierarchy so that threshold still works...
    """
    EMERGENCY = 80
    ALERT = 70
    CRITICAL = 60
    ERROR = 50
    WARNING = 40
    NOTICE = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

_nameToLogLevel = {
    "EMERGENCY" : LOG_LEVEL.EMERGENCY,
    "ALERT" : LOG_LEVEL.ALERT,
    "CRITICAL" : LOG_LEVEL.CRITICAL,
    "ERROR" : LOG_LEVEL.ERROR,
    "WARNING" : LOG_LEVEL.WARNING,
    "NOTICE" : LOG_LEVEL.NOTICE,
    "INFO" : LOG_LEVEL.INFO,
    "DEBUG" : LOG_LEVEL.DEBUG,
    "NOTSET" : LOG_LEVEL.NOTSET
}
""" log level string to internal log level int"""

IGNORED_ATTRS = (
    "id",       # gelf spec
    "args",     # logRecord 
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "message",
    "module",
    "msecs",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
)
""" attributes to be ignored 
 - gelf spec 
 - python logRecord attr 
"""

def _parseLogLevel(level: Union[int,str]):
    """ parse log level int/string and return its log level int

    Args:
        level (int | str): log level label
    Returns:
        int: log level int
    """
    if isinstance(level, int):
        logLevel = level
    elif isinstance(level, str):
        if level not in _nameToLevel:
            raise ValueError("Unknown level: %r" % level)
        logLevel = _nameToLogLevel[level]
    else:
        raise TypeError("Invalid log level input type: %r" % level)
    return logLevel


def _add_prefix(str: str) -> str:
    """ add "_" prefix to string

    Args:
        str (str): targeted string
    Returns:
        str: prefixed string item
    """
    if str[0] != "_":
        return "_%s" % str
    else: 
        return str


class Logger:
    """ Main logger object wrap from python logging
    """

    def __init__(self, level="DEBUG", extra=dict()):
        """

        Args:
            level (str, optional): log level. Defaults to LOG_LEVEL.DEBUG.
            extra (dict, optional): extra fields. Defaults to no extra field.
        """
        # Init Logger
        self.logger = logging.getLogger('vara_log')

        # prepare log level
        logging.addLevelName(LOG_LEVEL.DEBUG, "DEBUG")
        logging.addLevelName(LOG_LEVEL.INFO, "INFO")
        logging.addLevelName(LOG_LEVEL.NOTICE, "NOTICE")
        logging.addLevelName(LOG_LEVEL.WARNING, "WARNING")
        logging.addLevelName(LOG_LEVEL.ERROR, "ERROR")
        logging.addLevelName(LOG_LEVEL.CRITICAL, "CRITICAL")
        logging.addLevelName(LOG_LEVEL.ALERT, "ALERT")
        logging.addLevelName(LOG_LEVEL.EMERGENCY, "EMERGENCY")

        self.set_level(level)

        # Set formatter
        self._extra_fields : dict[str, Union[int, str]] = extra
        self._handler = logging.StreamHandler(stream=sys.stdout)
        self._handler.setFormatter(GELFFormatter(self._extra_fields))

        self.logger.addHandler(self._handler)

    
    def add_fields(self, fields: dict):
        """ add predefined extra log fields
        TODO: 
        - guard types?

        NOTE:
        for update formatter after logger inited
        https://stackoverflow.com/questions/6847862/how-to-change-the-format-of-logged-messages-temporarily-in-python

        """
        if not fields:
            return

        #self.logger.handlers[0].formatter.add_fields(fields)
        self._extra_fields.update(fields)
        self._handler.setFormatter(GELFFormatter(self._extra_fields))

    def remove_fields(self, keys: list):
        """ remove configured extra fields 
        """
        for k in keys:
            if k in self._extra_fields:
                self._extra_fields.pop(k)
                self._handler.setFormatter(GELFFormatter(self._extra_fields))

    
    def set_level(self, level: str):
        self.logger.setLevel(_parseLogLevel(level))

    def get_logger(self): 
        return self.logger


    #=== Log funcs ===
    def debug(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.DEBUG, msg, extra_fields)

    def info(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.INFO, msg, extra_fields)

    def notice(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.NOTICE, msg, extra_fields)

    def warning(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.WARNING, msg, extra_fields)

    def err(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.ERROR, msg, extra_fields)

    def crit(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.CRITICAL, msg, extra_fields)

    def alert(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.ALERT, msg, extra_fields)

    def emerg(self, msg, extra_fields={}):
        """
        Args:
            msg (str): log msg
            extra (dict, optional): optional fields
        """
        self.log(LOG_LEVEL.EMERGENCY, msg, extra_fields)

    def log(self, level:int, msg:Union[int, str], extra_fields={}):
        """ wrapper common log func

        Args:
            level (int): log level
            msg (int|str): log messege
            extra_fields (dict, optional): _description_. Defaults to {}.

        """

        try:
            self.logger.log(level, msg, extra=extra_fields)
        except Exception as err:
            # TODO: better handling
            print('Exception in trying to log: ', err)

class GELFFormatter(logging.Formatter):
    """ GELF formatter
    
    version
    host
    short_message
    full_message
    timestamp
    level
    _<extra optional fields>
    TODO: for optional fields
        - support predefined fields in config/ module init


    https://github.com/joaodrp/gelf-formatter

    Args:
        logging (logging.Formatter): _description_
    
    """

    def __init__(self, extra: dict):
        """
        Args:
            extra (dict): optional fields
        """
        super(GELFFormatter, self).__init__()
        self._hostname = socket.gethostname()

        # predefined extra fields
        self._extra_fields = extra

    def add_fields(self, fields: dict):
        self._extra_fields.update(fields)

    def remove_field(self, key: str):
        if key in self._extra_fields:
            self._extra_fields.pop(key)

    def format(self, record):
        """ convert to GELF format string

        Args:
            record (logging.LogRecord): raw log record to be formatted
        
        Returns:
            str: GELF formatted json string 
        """

        log_msg = dict()

        #=== Must have fields 
        log_msg["version"] = GELF_VERSION
        
        log_msg["host"] = self._hostname

        # By requirement, don't seperate short/full msg
        log_msg["message"] = record.getMessage()

        # log_msg["short_message"] = record.getMessage()

        # # full msg, traceback info if exist, otherwise just use the raw msg?
        # full_msg_str = ""
        # if record.exc_info is not None:
        #     full_msg_str = self.formatException(record.exc_info)
        # else:
        #     full_msg_str = record.getMessage()

        # log_msg["full_message"] = full_msg_str

        log_msg["timestamp"] = record.created
        
        # need to map levelname to cutom level int
        log_msg["level"] = _nameToLevel[record.levelname]

        #=== Optional fields
        # - predefined fields
        # - extra fields at logging event
        # https://stackoverflow.com/questions/56559971/show-extra-fields-when-logging-to-console-in-python
        # logging event override predefined fields, if attr key is it ok???
        # TODO: 
        # - guard attr value type parsing
        # - currently need to create and filter dict everytime, any better implementation??? 
        
        extra = dict()        
        extra.update(self._extra_fields)   # predefined fields
        extra.update(record.__dict__)     # at logging event

        for key, value in extra.items():
            if key not in IGNORED_ATTRS:    # filter unwanted entries
                log_msg[_add_prefix(key)] = str(value)


        return json.dumps(log_msg)
