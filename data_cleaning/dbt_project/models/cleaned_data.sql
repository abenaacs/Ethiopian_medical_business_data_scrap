WITH source_data AS (
    SELECT id, text
    FROM raw_data
),
deduplicated_data AS (
    SELECT DISTINCT id, text
    FROM source_data
    WHERE text IS NOT NULL AND LENGTH(text) > 0
)
SELECT * FROM deduplicated_data;