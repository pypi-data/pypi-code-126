import pandas as pd
import yfinance as yf


def yf_history(ticker: str, period: str = "max") -> pd.DataFrame:
    return yf.Ticker(ticker).history(period=period, auto_adjust=False)
