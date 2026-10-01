import pandas as pd
from twelvedata import TDClient
from twelvedata.exceptions import TwelveDataError


def fetch_time_series(
    api_key: str, symbol: str, interval: str, outputsize: int
) -> pd.DataFrame:
    """Fetch OHLC time series data from TwelveData.

    Args:
        api_key (str): The providers api key
        symbol (str): The financial symbol [Forex: EUR/USD, Stocks: APPL, Crypto: BTC/USD]
        interval (str): Time interval (e.g. "1min", "1H", "1day")
        outputsize (int): Number of rows/records to fetch

    Returns:
        pd.DataFrame: OHLC data with columns [datetime, open, high, low, close]
    """

    client = TDClient(apikey=api_key)

    try:
        time_series_data = client.time_series(
            symbol=symbol, interval=interval, outputsize=outputsize
        )
        df = time_series_data.as_pandas()
    except TwelveDataError as e:
        raise RuntimeError(f"TwelveData API request failed for {symbol}: {e}") from e

    if df is None or df.empty:
        raise ValueError(f"No data returned for symbol={symbol}, interval={interval}")

    return df
