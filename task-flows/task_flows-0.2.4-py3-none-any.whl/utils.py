import os
import re
from functools import cache
from pathlib import Path
from typing import List

import sqlalchemy as sa
from ready_logger import get_logger
from sqlalchemy.engine import Engine

from . import tables

logger = get_logger("task-flows")
systemd_dir = Path.home() / ".config/systemd/user"


# TODO switch this to nullpool engine in class instance?
@cache
def get_engine(var_name="POSTGRES_URL") -> Engine:
    """Create an Sqlalchemy engine using a Postgresql URL from environment variable."""
    if not (url := os.getenv(var_name)):
        raise RuntimeError(
            f"Environment variable {var_name} is not set. Can not connect to database."
        )
    return sa.create_engine(url)


def get_tasks_systemd_files() -> List[Path]:
    """Get all systemd files from existing tasks."""
    return list(systemd_dir.glob("task_flow_*"))


def get_file_task_name(file: Path):
    """Extract task name from a systemd file."""
    return re.sub("^task_flow_", "", file.stem)


def get_existing_task_names() -> List[str]:
    """Get names of all tasks that have been created."""
    return [get_file_task_name(f) for f in get_tasks_systemd_files()]


def get_scheduled_names():
    """Get names of all scheduled tasks."""
    with get_engine().begin() as conn:
        scheduled_names = set(
            conn.execute(
                sa.select(tables.timer_options_table.c.task_name.distinct())
            ).scalars()
        )
    return scheduled_names
