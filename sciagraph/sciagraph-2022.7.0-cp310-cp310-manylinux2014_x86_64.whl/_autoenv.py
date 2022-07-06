"""
Infrastructure for automatically running sciagraph based on an environment
variable, and for automatic initialization on startup.
"""

import os
import sys
import logging
import ctypes


def _check_user_configured_mode_via_env_var():
    """
    Translate a SCIAGRPAH_MODE environment variable into the relevant
    ``python -m sciagraph`` command-line options.

    This will run in the original process started by the user.
    """
    mode = os.environ.pop("SCIAGRAPH_MODE", None)
    if mode is None:
        return
    if mode not in {"process", "api"}:
        logging.error(
            "The SCIAGRAPH_MODE environment variable only supports the values"
            f" 'process' and 'api', but you set it to {mode!r}, exiting."
        )
        os._exit(1)

    import ctypes

    # TODO: Python 3.10 and later have sys.orig_argv.
    _argv = ctypes.POINTER(ctypes.c_wchar_p)()
    _argc = ctypes.c_int()
    ctypes.pythonapi.Py_GetArgcArgv(ctypes.byref(_argc), ctypes.byref(_argv))
    argv = _argv[: _argc.value]
    args = ["python", "-m", "sciagraph", f"--mode={mode}", "run"] + argv[1:]

    os.execv(sys.executable, args)


_check_user_configured_mode_via_env_var()


def _check_initialization():
    """
    Initialize Sciagraph inside a new process.

    This will run in the final, runtime process created by ``python -m sciagraph run``.
    """
    value = os.environ.pop("__SCIAGRAPH_INITIALIZE", None)
    if value is None:
        return

    if value in ("process", "api"):
        exe = ctypes.PyDLL(None)
        initialize = exe.sciagraph_initialize
        initialize.argtypes = [ctypes.c_int]
        initialize.restype = None
        initialize(1 if value == "process" else 0)
        return

    logging.error(f"__SCIAGRAPH_INITIALIZE is {value}, this is a bug.")
    os._exit(1)


_check_initialization()
