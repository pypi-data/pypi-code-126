
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rocketry import Session

class RedBase:
    """Baseclass for all Red Engine classes"""
    session: 'Session' = None