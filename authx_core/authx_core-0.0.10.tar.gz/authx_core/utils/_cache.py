from authx_core._async._async_session import get_engine as authxAsyncGetEngine
from authx_core._async._async_session import (
    get_sessionmaker as authxAsyncGetSessionmaker,
)
from authx_core.model._settings import _api_settings as authxApiSettings
from authx_core.settings._database import get_database_settings as authxDatabaseSettings


def clear_caches() -> None:
    """Clear all caches a function used to run all the  `lru_cache` decorators."""
    authxApiSettings.cache_clear()
    authxDatabaseSettings.cache_clear()
    authxAsyncGetEngine.cache_clear()
    authxAsyncGetSessionmaker.cache_clear()
