from pathlib import Path
import polars as pl
import pyarrow.dataset as ds

def read_csv(path_input: Path) -> pl.LazyFrame:

    # Log - starting process:
    print(f'Attempt to read: {path_input}')

    # Read CSV w/ Polars:
    csv_data = pl.scan_csv(
        source=path_input
    )
    print(f'Scanned .csv sucessfully!')
    
    return csv_data

def write_parquet(lazy_frame: pl.LazyFrame, path_output: Path, partition_by_ordered_cols: list[str] = None) -> dict[str, Path | int]:
    
    # Check if partition is valid:
    if partition_by_ordered_cols is not None:
        cols = lazy_frame.collect_schema().names()
        for column in partition_by_ordered_cols:
            assert column in cols, f'Partition column {column} not found in data!'
    
    # Collecting LazyFrame:
    collected_frame = lazy_frame.collect()

    # Data Info:
    row_count, col_count = collected_frame.shape
    print(f'Rows: {row_count:_}\nCols: {col_count:_}')

    # Converting Polars LazyFrame -> PyArrow Dataset:
    arrow_table = collected_frame.to_arrow()

    # Writing in parquet:
    print(f'Attempt to write data into .parquet on path: {path_output}')
    ds.write_dataset(
        data=arrow_table,
        base_dir=path_output,
        format='parquet',
        partitioning=partition_by_ordered_cols,
        partitioning_flavor='hive',
        existing_data_behavior='overwrite_or_ignore', # Replace or ignore the record
        create_dir=True
    )

    # Checking:
    recently_written_file = pl.scan_parquet(
        source=f'{path_output.as_posix()}/**/*.parquet'
    )

    assert recently_written_file.select(pl.len()).collect().item() == row_count, 'Error - the number of rows appended does not match the original input!'
    
    print(f'Parquet file(s) saved on output path - {path_output}')

    return {'path': path_output, 'row_count': row_count}