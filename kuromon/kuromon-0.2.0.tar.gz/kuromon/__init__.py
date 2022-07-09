try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

from .kuromon import to_table  # noqa: F401

__version__ = importlib_metadata.version(__name__)
