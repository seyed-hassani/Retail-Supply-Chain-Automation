
SELECT
    i.sku_id,
    i.stock_level,
    i.reorder_point,
    s.product_name,
    CASE 
        WHEN i.stock_level <= i.reorder_point THEN 'REORDER'
        ELSE 'STOCK_OK'
    END AS stock_status
FROM {{ ref('stg_sales') }} s
JOIN {{ source('raw', 'inventory') }} i
  ON s.sku_id = i.sku_id
