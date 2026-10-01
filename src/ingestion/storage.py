# save_to_storage() , load_from_storage()

from pathlib import Path

import pandas as pd


def save_to_storage(
    data: pd.DataFrame, storage_path: str, file_type: str = "csv"
) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        storage_path (str): _description_
        file_type (str, optional): _description_. Defaults to "csv".

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """

    dir_path = Path("data") / storage_path

    dir_path.mkdir(parents=True, exist_ok=True)

    file_path: str = (
        dir_path / f"raw_data.{file_type}"
    )  # update to include symbol or evens partitiion it

    match file_type.strip().lower():
        case "csv":
            data.to_csv(path_or_buf=file_path, index=True)

        case "json":
            data.to_json(path_or_buf=file_path, index=True, indent=4)

        case "parquet":
            data.to_parquet(path_or_buf=file_path, index=True)

        case _:
            raise ValueError(
                f"Unsupported file type: {file_type}. Must be csv, json and parquet"
            )

    return file_path
