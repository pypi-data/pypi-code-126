import logging

from fastapi import APIRouter, Depends

from simplefancontroller.sfc import SimpleFanController
from simplefancontroller.api.user_manager import SFCUserManager
from simplefancontroller.sfc.data_manager import SFCDataManager
from ..jwt_bearer import JWTBearer

logger = logging.getLogger(__name__)
controller_router = APIRouter(
    dependencies=[Depends(JWTBearer())], tags=["controller"], prefix="/api/v1"
)
CONTROLLER = SimpleFanController()
USER_MANAGER = SFCUserManager()
DATA_MANAGER = SFCDataManager()


@controller_router.on_event("startup")
def initialize_controller():
    """Import data on FastAPI app start."""
    try:
        CONTROLLER.import_data()
    except FileNotFoundError:
        logger.info("No configuration file found. Using default values instead.")


@controller_router.on_event("shutdown")
def shutdown_controller():
    """Shutdown the controller on exit."""
    CONTROLLER.shutdown()
    CONTROLLER.export_data()
    DATA_MANAGER.shutdown()
    USER_MANAGER.shutdown()


@controller_router.get("/cpu-temperature", response_model=float)
def get_temperature():
    """Get current CPU temperature."""
    return CONTROLLER.current_temperature
