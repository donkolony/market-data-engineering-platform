from pandas import pd

from src.config import EXPECTED_SCHEMA

x = EXPECTED_SCHEMA


def validate_schema(df: pd.DataFrame) -> None:
    # check the expected schema vs the once being fetched
    pass


def validate_no_nulls(df: pd.DataFrame) -> None:
    pass


def validate_ohlc_consistency(df: pd.DataFrame) -> None:
    pass


def validate_no_duplicate_timestamps(df: pd.DataFrame) -> None:
    if not df["datetime"].is_unique:
        duplicates = df[df["datetime"].duplicated()]["datetime"].tolist()
        raise ValueError(f"Duplicated timestamps found: {duplicates[:5]}....")


def validate_sorted_by_datetime(df: pd.DataFrame) -> None:
    pass


def check_price_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    pass


def ensure_datetime_dtype(df: pd.DataFrame) -> pd.DataFrame:
    pass


# ochestrator for all validation functions
def validate_market_data(df: pd.DataFrame) -> pd.DataFrame:
    # call or the validation steps (function) in orrder
    df = ensure_datetime_dtype(df)
    validate_schema(df)
    validate_no_nulls(df)
    validate_no_duplicate_timestamps(df)
    validate_ohlc_consistency(df)
    validate_sorted_by_datetime(df)

    anomalies = check_price_anomalies(df)

    if not anomalies.empty:
        print(
            f"{len(anomalies)} rows with suspicous price moves"
        )  # TODO use logger instead of print

    return df
