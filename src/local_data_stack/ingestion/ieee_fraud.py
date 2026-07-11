import polars as pl
from pathlib import Path
from local_data_stack.config import get_data_layer_paths
from local_data_stack.io_utils import read_csv, write_parquet

def ingest_transaction() -> dict[str | Path | int]:

    # Locate paths:
    dic_path = get_data_layer_paths()
    raw_dir = dic_path['raw']
    bronze_dir = dic_path['bronze']
    transaction_csv_path = raw_dir / 'ieee-fraud-detection' / 'train_transaction.csv'

    # Transaction Data
    transaction_lazy_frame = read_csv(transaction_csv_path)
    transaction_lazy_frame_partitioned = (
        transaction_lazy_frame
        .with_columns(
            (pl.col('TransactionDT')/86400).cast(pl.Int64).alias('TransactionDT_RELATIVE_DAY')
        )
    )
    result = write_parquet(
        lazy_frame=transaction_lazy_frame_partitioned,
        path_output=bronze_dir / 'transaction',
        partition_by_ordered_cols=['TransactionDT_RELATIVE_DAY']
    )

    return result

def ingest_identity() -> dict[str | Path | int]:

    # Locate paths:
    dic_path = get_data_layer_paths()
    raw_dir = dic_path['raw']
    bronze_dir = dic_path['bronze']
    identity_csv_path = raw_dir / 'ieee-fraud-detection' / 'train_identity.csv'

    # Identity Data
    identity_lazy_frame = read_csv(identity_csv_path)
    result = write_parquet(
        lazy_frame=identity_lazy_frame,
        path_output=bronze_dir / 'identity',
    )

    return result

if __name__ == '__main__':
    ingest_transaction()
    ingest_identity()