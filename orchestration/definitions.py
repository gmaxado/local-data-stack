import dagster as dg
from orchestration.assets import bronze_identity, bronze_transaction, dbt_models
from orchestration.dbt_project import dbt_project
from dagster_dbt import DbtCliResource

defs = dg.Definitions(assets=[bronze_transaction, bronze_identity, dbt_models], resources={"dbt": DbtCliResource(project_dir=dbt_project)})