from typing import Optional

import FinanceDataReader as fdr
import pandas as pd


def time_series(
    ticker: str,
    sdate: Optional[str] = None,
    edate: Optional[str] = None,
    exchange: Optional[str] = None,
) -> pd.DataFrame:
    return fdr.DataReader(
        symbol=ticker, start=sdate, end=edate, exchange=exchange
    )


def fred_time_series(
    ticker: str,
    sdate: Optional[str] = None,
    edate: Optional[str] = None,
) -> pd.DataFrame:
    return fdr.DataReader(
        symbol=ticker, start=sdate, end=edate, data_source="FRED"
    )
