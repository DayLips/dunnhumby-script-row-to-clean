TRUNCATE TABLE clean.hh_demographic RESTART IDENTITY;

INSERT INTO clean.hh_demographic (
    household_key, age_desc, marital_status, income_desc, homeowner_desc,
    hh_comp_desc, household_size_desc, kid_category_desc,
    household_size_numeric, has_kids, is_retired
)
SELECT
    household_key,
    NULLIF(TRIM(age_desc), '') AS age_desc,
    CASE UPPER(TRIM(marital_status_code))
        WHEN 'A' THEN 'Married'
        WHEN 'B' THEN 'Single'
        ELSE NULL
    END AS marital_status,
    NULLIF(TRIM(income_desc), '') AS income_desc,
    NULLIF(TRIM(homeowner_desc), '') AS homeowner_desc,
    NULLIF(TRIM(hh_comp_desc), '') AS hh_comp_desc,
    NULLIF(TRIM(household_size_desc), '') AS household_size_desc,
    NULLIF(TRIM(kid_category_desc), '') AS kid_category_desc,
    CAST(REGEXP_REPLACE(household_size_desc, '^(\d+).*$', '\1') AS INTEGER) AS household_size_numeric,
    CASE WHEN kid_category_desc IS NOT NULL AND UPPER(TRIM(kid_category_desc)) != 'NO KIDS' THEN TRUE ELSE FALSE END AS has_kids,
    CASE WHEN age_desc = '65+' THEN TRUE ELSE FALSE END AS is_retired
FROM raw.hh_demographic
WHERE household_key IS NOT NULL;