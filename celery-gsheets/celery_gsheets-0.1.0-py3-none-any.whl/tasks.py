from decouple import config

from .celery import app
from .pygsheets import *

SPREADSHEET_TITLE = config('SPREADSHEET_TITLE')
SERVICE_ACCOUNT_FILE = config('SERVICE_ACCOUNT_FILE', None)
SERVICE_ACCOUNT_ENV_VAR = config('SERVICE_ACCOUNT_ENV_VAR', None)

doc = Spreadsheet.open(
    SPREADSHEET_TITLE,
    service_account_env_var=SERVICE_ACCOUNT_ENV_VAR,
    service_account_file=SERVICE_ACCOUNT_FILE,
)


def gs_write(*args, **kwargs):
    return gs_write_method.delay(*args, **kwargs)


@app.task(max_retries=None, rate_limit='1/s')
def gs_write_method(ws_title, method, *args, **kwargs):
    ws: Worksheet = doc.worksheet(ws_title)
    print(ws_title, method, *args, kwargs, sep=', ')
    getattr(ws, method)(*args, **kwargs)
    return True
