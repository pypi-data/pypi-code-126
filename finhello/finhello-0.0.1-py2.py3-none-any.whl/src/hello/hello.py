import functools
import inspect
import logging
import sys
import timeit
from logging.handlers import RotatingFileHandler
from os import getpid
import os
from time import sleep

from flask import Flask, request

logger = logging.getLogger(__name__)

app = Flask(__name__)

process_name = os.environ.get("SUPERVISOR_PROCESS_NAME", "hello")
logging.basicConfig(level=logging.INFO)
logger.addHandler(RotatingFileHandler("logfile{}.log".format(process_name), maxBytes=10 * 1024 * 1024, backupCount=2))

wlogger = logging.getLogger('waitress')
wlogger.addHandler(RotatingFileHandler("waitress{}.log".format(process_name), maxBytes=10 * 1024 * 1024, backupCount=2))


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


@app.route("/")
@log_timing
def hello():
    id__ = str(getpid())
    logger.info("{} handled in a process {}".format(request, id__))
    version = ".".join(map(str, sys.version_info[:3]))
    return "Hello, World! Process {}, python version {}".format(id__, version)


@app.route('/sleep/<seconds>', methods=['GET'])
def hardwork(seconds):
    logger.info("Sleep for {} seconds".format(seconds))
    sleep(int(seconds))
    logger.info("Wake up after {} seconds".format(seconds))
    id__ = str(getpid())
    return "Process {}".format(id__)


def wsgi_app(env, start_response):
    id__ = str(getpid())
    logger.info("Request handled in a process {}".format(id__))
    start_response("200 OK", [("Content-Type", "text/html")])

    return [b"Hello World"]


if __name__ == "__main__":
    from waitress import serve

    # app.run(host="0.0.0.0", port=5000)
    # serve(wsgi_app, host="0.0.0.0", port=5000)

    serve(app, host="0.0.0.0", port=5050)
