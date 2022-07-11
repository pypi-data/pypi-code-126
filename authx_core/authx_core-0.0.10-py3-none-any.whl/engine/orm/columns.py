from datetime import datetime

import sqlalchemy as sa


def created_at_column() -> "sa.Column[datetime]":
    return sa.Column(
        sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
    )


def updated_at_column() -> "sa.Column[datetime]":
    return sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False,
    )
