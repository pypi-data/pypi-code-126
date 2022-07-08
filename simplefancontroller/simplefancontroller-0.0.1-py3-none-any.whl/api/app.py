from fastapi import FastAPI

from simplefancontroller.api.routers.controller import controller_router
from simplefancontroller.api.routers.fans import fan_router
from simplefancontroller.api.routers.settings import settings_router
from simplefancontroller.api.routers.auth import auth_router


def generate_api():
    app = FastAPI()
    for router in [controller_router, fan_router, settings_router, auth_router]:
        app.include_router(router)
    return app


app = generate_api()
