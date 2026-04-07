-- Query 1: Island Areas
-- Purpose: Calculate island areas in square kilometers

-- Requirements:
-- - Filter places_a where fclass = 'island'
-- - Use ST_Area(geom::geography) for accurate measurements on WGS84
-- - Convert square meters to square kilometers (divide by 1,000,000)
-- - Order results by area (largest first)
-- - Include geom column for spatial visualization in GeoPandas

-- Expected Output:
-- - name
-- - area_sq_km

SELECT
    name,
    ST_Area(geom::geography) / 1000000 AS area_sq_km,
    geom
FROM
    places_a
WHERE
    fclass = 'island'
ORDER BY
    area_sq_km DESC;