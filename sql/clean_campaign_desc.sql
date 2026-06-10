TRUNCATE TABLE clean.campaign_desc RESTART IDENTITY;

INSERT INTO clean.campaign_desc (campaign, campaign_type, start_day, end_day, campaign_duration_days)
SELECT
    campaign,
    CASE
        WHEN UPPER(TRIM(description)) = 'TYPEA' THEN 'A'
        WHEN UPPER(TRIM(description)) = 'TYPEB' THEN 'B'
        WHEN UPPER(TRIM(description)) = 'TYPEC' THEN 'C'
        ELSE NULL
    END AS campaign_type,
    start_day,
    end_day,
    (end_day - start_day) AS campaign_duration_days
FROM raw.campaign_desc
WHERE campaign IS NOT NULL
  AND start_day IS NOT NULL
  AND end_day IS NOT NULL
  AND start_day <= end_day;