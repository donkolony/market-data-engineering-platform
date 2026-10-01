# The orhestrator. The GLUE

from src.config import API_KEY, FILE_TYPE, INTERVAL, OUTPUT_SIZE, STORAGE_PATH, SYMBOL
from src.ingestion.client import fetch_time_series
from src.ingestion.storage import save_to_storage


def main():
    print("Hello from market-data-engineering-platform!")


if __name__ == "__main__":
    api_client = fetch_time_series(
        api_key=API_KEY, symbol=SYMBOL, interval=INTERVAL, outputsize=OUTPUT_SIZE
    )

    storage_path = STORAGE_PATH
    file_type = FILE_TYPE

    save_to_storage(data=api_client, storage_path=storage_path, file_type=file_type)
