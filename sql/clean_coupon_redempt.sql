TRUNCATE TABLE clean.coupon_redempt RESTART IDENTITY;

INSERT INTO clean.coupon_redempt (household_key, day, coupon_upc, campaign_id, household_valid, coupon_campaign_valid)
SELECT
    t.household_key,
    t.day,
    t.coupon_upc,
    t.campaign_id,
    CASE WHEN hh.household_key IS NOT NULL THEN TRUE ELSE FALSE END AS household_valid,
    CASE WHEN c.coupon_upc IS NOT NULL THEN TRUE ELSE FALSE END AS coupon_campaign_valid
FROM raw.coupon_redempt t
LEFT JOIN clean.hh_demographic hh ON t.household_key = hh.household_key
LEFT JOIN clean.coupon c ON t.coupon_upc = c.coupon_upc AND t.campaign_id = c.campaign_id
WHERE t.household_key IS NOT NULL
  AND t.day IS NOT NULL
  AND t.coupon_upc IS NOT NULL
  AND t.campaign_id IS NOT NULL;