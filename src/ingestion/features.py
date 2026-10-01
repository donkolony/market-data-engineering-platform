# feature engineering, called after validation passes

import pandas as pd


def time_series(df: pd.DataFrame) -> pd.DataFrame:
    pass


def price_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def return_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def rolling_statistics(df: pd.DataFrame) -> pd.DataFrame:
    pass


def volitity_features() -> pd.DataFrame:
    pass


def lag_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def moving_average(df: pd.DataFrame) -> pd.DataFrame:
    pass


def session_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def data_quality_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def technical_indicator_features(df: pd.DataFrame) -> pd.DataFrame:
    pass


def feature_engineer(df: pd.DataFrame) -> pd.DataFrame:

    df = return_features(df)

    df = lag_features(df)

    df = moving_average(df)

    df = data_quality_features(df)

    return df
