"""python 
1. Schema validation - column names, types and  ensure that the structure matches what I expcted
expected_schema = {
    "datetime": "datetime64[ns]",
    "open": "float64",
    "high":"float64",
    "low": "float64",
    "close": "float"
}

2. Null/completeness checks
assert df.isnull().sum() == 0 , "Unexpected nulls in OHLC data

3. Duplicate detection (this can be caused via API/retry artifact)
assert df["datetime].is_unique, "Duplicate timestamps found"

4. Domain.business logic checks - ensure that prices like high is actually higher than the low and vise versa
assert (df['high'] >= df['low']).all(), "high < low somewhere"
assert (df['high'] >= df['open']).all()
assert (df['high'] >= df['close']).all()
assert (df['low'] <= df['open']).all()
assert (df['low'] <= df['close']).all()
assert (df[['open', 'high', 'low', 'close']] > 0).all().all(), "Non-positive prices"

5. Range/sanity checks - bounds that flag garbage data without hardcoding business logic. e.g., flag (not necessarily fail) extreeme single bar moves
pct_change = df['close'].pct_change().abs()
suspicious = df[pct_change > 0.20]  # tune threshold per instrument

6. Time series continuity 
df = df.sort_values('datetime')
gaps = df['datetime'].diff().value_counts()
s
7. Order/monotonicity
assert df['datetime'].is_monotonic_increasing, "Data not sorted by datetime"


validate*_ -> returns None
check*_ -> returns a boolean
ensure*_ -> returns a DataFrame
"""


 