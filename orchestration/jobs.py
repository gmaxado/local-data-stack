import dagster as dg
from orchestration.assets import bronze_transaction, bronze_identity, dbt_models

ieee_fraud_job = dg.define_asset_job(
    name="ieee_fraud_job",
    selection=[bronze_transaction, bronze_identity,dbt_models]
)