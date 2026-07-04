from pathlib import Path
import polars as pl
from local_data_stack.config import get_data_layer_paths
from local_data_stack.io_utils import read_csv_to_parquet

DIC_PATH = get_data_layer_paths()