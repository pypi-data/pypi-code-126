from fastapi import APIRouter, Depends, HTTPException

from simplefancontroller.sfc import SFControllerSettings, SFCDBSettings
from .controller import CONTROLLER
from ..jwt_bearer import JWTBearer

settings_router = APIRouter(
    dependencies=[Depends(JWTBearer())], tags=["controller"], prefix="/api/v1/settings"
)


@settings_router.get("", response_model=SFControllerSettings)
async def get_settings():
    """Get the current SFController settings."""
    return CONTROLLER.settings


@settings_router.put("")
async def update_settings(settings: SFControllerSettings):
    """Update the SFController settings."""
    CONTROLLER.settings = settings


@settings_router.get("/persistence", response_model=list[SFCDBSettings])
async def get_persistence_settings():
    """Get the current persistence settings."""
    return CONTROLLER.settings.persistence_settings


@settings_router.post("/persistence")
async def add_persistence(settings: SFCDBSettings):
    """Adds settings for a database client."""
    CONTROLLER.settings[settings.name] = settings


@settings_router.put("/persistence/{name}")
async def update_persistence(name: str, settings: SFCDBSettings):
    """Updates the settings for a database client."""
    if name not in CONTROLLER.db_clients:
        raise HTTPException(
            status_code=500, detail=f"No database client with name {name} found."
        )
    CONTROLLER.update_db_client(name, settings)


@settings_router.delete("/persistence/{id}")
async def delete_persistence_settings(id: str):
    """Update the current persistence settings."""
    CONTROLLER.data_manager.delete_persistence(id)
