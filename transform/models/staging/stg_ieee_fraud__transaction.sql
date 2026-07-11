with source as (
    select * from {{ source('ieee_fraud','transaction') }}
)

select

    TransactionID as transaction_id,
    isFraud as is_fraud,
    TransactionDT as transaction_dt,
    TransactionAmt as transaction_amt,
    ProductCD as product_cd,
    card1 as card1,
    card2 as card2,
    card3 as card3,
    card4 as card4,
    card5 as card5,
    card6 as card6,
    addr1 as addr1,
    addr2 as addr2,
    dist1 as dist1,
    dist2 as dist2,
    P_emaildomain as p_emaildomain,
    R_emaildomain as r_emaildomain,
    COLUMNS('^C\d+$'),
    COLUMNS('^D\d+$'),
    COLUMNS('^M\d+$'),
    COLUMNS('^V\d+$'),

from source