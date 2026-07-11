import dagster as dg
from local_data_stack.ingestion.ieee_fraud import ingest_transaction, ingest_identity
from dagster_dbt import DbtCliResource, dbt_assets
from orchestration.dbt_project import dbt_project

@dg.asset
def bronze_transaction() -> dg.MaterializeResult:
    result = ingest_transaction()

    return dg.MaterializeResult(
        metadata={
            "row_count": dg.MetadataValue.int(result["row_count"]),
            "output_path": dg.MetadataValue.path(str(result["path"])),
        }
    )

@dg.asset
def bronze_identity() -> dg.MaterializeResult:
    result = ingest_identity()

    return dg.MaterializeResult(
        metadata={
            "row_count": dg.MetadataValue.int(result["row_count"]),
            "output_path": dg.MetadataValue.path(str(result["path"])),
        }
    )

@dbt_assets(manifest= dbt_project.manifest_path)
def dbt_models(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream().fetch_row_counts()