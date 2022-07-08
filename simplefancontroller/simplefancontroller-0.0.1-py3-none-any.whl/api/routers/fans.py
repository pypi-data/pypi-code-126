from fastapi import APIRouter, HTTPException, Depends

from simplefancontroller.sfc import SFCFan, SFCFanSettings, SFCFanState
from .controller import CONTROLLER
from ..jwt_bearer import JWTBearer

fan_router = APIRouter(
    dependencies=[Depends(JWTBearer())], tags=["fans"], prefix="/api/v1/fans"
)


@fan_router.get("", response_model=list[SFCFanSettings])
async def get_fans():
    """Get a list of all stored SFCFans."""
    return CONTROLLER.fans.get_fans()


@fan_router.get("/status", response_model=list[SFCFanState])
async def get_status_all():  #
    """Get the status of all stored SFCFans."""
    return CONTROLLER.fans.get_state()


@fan_router.get("/{id}", response_model=SFCFanSettings)
async def get_fan(id: str) -> SFCFanSettings:
    """Get a single SFCFan by its id."""
    try:
        return CONTROLLER.fans.get_fan(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Fan not found") from e


@fan_router.get("/{id}/status", response_model=SFCFanState)
async def get_status_single(id: str):
    """Get the status of a single SFCFan."""
    try:
        return CONTROLLER.fans.get_fans(id).state
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Fan not found") from e


@fan_router.post("")
async def add_fan(fan: SFCFanSettings):
    """Add a new SFCFan."""
    try:
        CONTROLLER.fans.add_fan(fan=SFCFan.from_settings(fan))
    except ValueError as e:
        raise HTTPException(
            status_code=500, detail=f"Fan with name {fan.name} already exists."
        ) from e


@fan_router.put("/{id}")
async def update_fan(id: str, fan: SFCFanSettings):
    """Update a SFCFan with new settings."""
    try:
        CONTROLLER.fans.update_fan(id, fan)
    except ValueError as e:
        raise HTTPException(
            status_code=500, detail=f"Fan with name {fan.name} already exists."
        ) from e


@fan_router.delete("/{id}")
async def remove_fan(id: str):
    """Delete a SFCFan."""
    try:
        CONTROLLER.fans.remove_fan(id)
    except ValueError as e:
        raise HTTPException(
            status_code=500, detail=f"Fan with name {id} already exists."
        ) from e
