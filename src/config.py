import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("TWELVEDATA_API_KEY")
SYMBOL = os.environ.get("SYMBOL")
INTERVAL = os.environ.get("INTERVAL")
OUTPUT_SIZE = int(os.environ.get("OUTPUT_SIZE"))
STORAGE_PATH = os.environ.get("STORAGE_PATH")
FILE_TYPE = os.environ.get("FILE_TYPE")


EXPECTED_SCHEMA = {}
