TRUNCATE TABLE clean.campaign_table RESTART IDENTITY;

INSERT INTO clean.campaign_table (household_key, campaign_id, campaign_type)
SELECT DISTINCT ON (household_key, campaign_id)
    household_key,
    campaign_id,
    CASE
        WHEN UPPER(TRIM(description)) = 'TYPEA' THEN 'A'
        WHEN UPPER(TRIM(description)) = 'TYPEB' THEN 'B'
        WHEN UPPER(TRIM(description)) = 'TYPEC' THEN 'C'
        ELSE NULL
    END AS campaign_type
FROM raw.campaign_table
WHERE household_key IS NOT NULL
  AND campaign_id IS NOT NULL
  AND EXISTS (SELECT 1 FROM clean.campaign_desc cd WHERE cd.campaign = campaign_id)