TRUNCATE TABLE clean.transaction_data RESTART IDENTITY;

INSERT INTO clean.transaction_data (
    basket_id,
    product_id,
    household_key,
    day,
    quantity,
    sales_value,
    store_id,
    trans_time,
    week_no,
    retail_disc,
    coupon_disc,
    coupon_match_disc,
    unit_price,
    total_discount,
    discount_rate,
    product_valid,
    household_valid,
    has_discount
)
SELECT
    t.basket_id,
    t.product_id,
    t.household_key,
    t.day,
    t.quantity,
    t.sales_value,
    t.store_id,
    t.trans_time,
    t.week_no,
    t.retail_disc,
    t.coupon_disc,
    t.coupon_match_disc,
    t.sales_value / NULLIF(t.quantity, 0) AS unit_price,
    COALESCE(t.retail_disc, 0) + COALESCE(t.coupon_disc, 0) + COALESCE(t.coupon_match_disc, 0) AS total_discount,
    CASE
        WHEN (t.sales_value - (COALESCE(t.retail_disc,0)+COALESCE(t.coupon_disc,0)+COALESCE(t.coupon_match_disc,0))) != 0
        THEN (COALESCE(t.retail_disc,0)+COALESCE(t.coupon_disc,0)+COALESCE(t.coupon_match_disc,0))
             / (t.sales_value - (COALESCE(t.retail_disc,0)+COALESCE(t.coupon_disc,0)+COALESCE(t.coupon_match_disc,0)))
        ELSE NULL
    END AS discount_rate,
    CASE WHEN p.product_id IS NOT NULL THEN TRUE ELSE FALSE END AS product_valid,
    CASE WHEN hh.household_key IS NOT NULL THEN TRUE ELSE FALSE END AS household_valid,
    (COALESCE(t.retail_disc,0) != 0 OR COALESCE(t.coupon_disc,0) != 0 OR COALESCE(t.coupon_match_disc,0) != 0) AS has_discount
FROM raw.transaction_data t
LEFT JOIN clean.products p ON t.product_id = p.product_id
LEFT JOIN clean.hh_demographic hh ON t.household_key = hh.household_key
WHERE t.quantity > 0
  AND t.sales_value >= 0
  AND t.day IS NOT NULL
  AND t.week_no IS NOT NULL
  AND t.basket_id IS NOT NULL
  AND t.product_id IS NOT NULL;