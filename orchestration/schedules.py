import dagster as dg
from orchestration.assets import dbt_models
from orchestration.jobs import ieee_fraud_job

daily_schedule = dg.ScheduleDefinition(
    name="daily_ieee_fraud",
    cron_schedule="0 0 * * *",  # Runs at midnight daily
    job=ieee_fraud_job
)