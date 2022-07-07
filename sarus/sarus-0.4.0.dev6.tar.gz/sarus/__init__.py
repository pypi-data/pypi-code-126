"""Sarus python SDK documentation."""
import nest_asyncio

from sarus import (
    numpy,
    pandas,
    pandas_profiling,
    plotly,
    sklearn,
    std,
    xgboost,
)

from .sarus import Client, Dataset
from .utils import eval, eval_policy, length

VERSION = "0.4.0.dev6"

__all__ = ["Dataset", "Client", "length", "eval", "eval_policy", "config"]


nest_asyncio.apply()
