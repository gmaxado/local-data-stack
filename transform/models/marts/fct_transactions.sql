{{ config(
            materialized='external',    
            location='data/gold/fct_transactions.parquet',
            format='parquet'
) }}

with transaction as (
    select * from {{ ref('stg_ieee_fraud__transaction') }}
),

identity as (
    select * from {{ ref('stg_ieee_fraud__identity') }}
)
select

    t.*,
    i.* EXCLUDE(transaction_id)

from transaction t
left join identity i
    on t.transaction_id = i.transaction_id