import logging
from typing import Literal

import pandas as pd
from numpy import nan

logger = logging.getLogger(__name__)


def set_dtypes(
    df: pd.DataFrame,
    schema: dict,
    on_missing_cols: Literal["warning", "skip", "add", "raise"] = "warning",
    date_cols: list = None,
) -> pd.DataFrame:

    missing_columns: set = set(schema.keys()) - set(df.columns)
    if missing_columns:
        if on_missing_cols == "warning":
            logger.warning(f"Missing columns: {missing_columns}")
            for col in missing_columns:
                schema.pop(col)
        elif on_missing_cols == "add":
            logger.warning(f"Missing columns: {missing_columns} -> filling with NaN")
            for col in missing_columns:
                df[col] = nan
        elif on_missing_cols == "raise":
            raise KeyError(f"Columns {missing_columns} not in DataFrame")

    df = df.astype(schema)
    # convert date cols to datetime.date object so that they are saved as
    # DATE type in parquet file
    if date_cols:
        for col in date_cols:
            df[col] = df[col].dt.date
    # order columns
    df = df[schema.keys()]

    return df
