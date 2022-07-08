from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from simplefancontroller.sfc.controller import SimpleFanController


controller = SimpleFanController()


def fastapi_factory(include_frontend: bool = True) -> FastAPI:
    app = FastAPI()

    return app
