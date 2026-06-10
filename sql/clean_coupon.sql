TRUNCATE TABLE clean.coupon RESTART IDENTITY;

INSERT INTO clean.coupon (coupon_upc, product_id, campaign_id, product_valid, campaign_valid)
SELECT DISTINCT
    t.coupon_upc,
    t.product_id,
    t.campaign_id,
    CASE WHEN p.product_id IS NOT NULL THEN TRUE ELSE FALSE END AS product_valid,
    CASE WHEN c.campaign IS NOT NULL THEN TRUE ELSE FALSE END AS campaign_valid
FROM raw.coupon t
LEFT JOIN clean.products p ON t.product_id = p.product_id
LEFT JOIN clean.campaign_desc c ON t.campaign_id = c.campaign
WHERE t.coupon_upc IS NOT NULL
  AND t.product_id IS NOT NULL
  AND t.campaign_id IS NOT NULL;