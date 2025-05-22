
WITH raw_sales AS (
    SELECT * FROM {{ source('raw', 'sales') }}
)
SELECT
    sale_id,
    sku_id,
    quantity,
    sale_date
FROM raw_sales
