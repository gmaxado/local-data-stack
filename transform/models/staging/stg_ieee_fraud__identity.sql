with source as (
    select * from {{ source('ieee_fraud','identity') }}
)

select

    TransactionID as transaction_id,
    DeviceType as device_type,
    DeviceInfo as device_info,
    COLUMNS('^id_')

from source