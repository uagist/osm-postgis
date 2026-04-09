-- Query 3: Restaurants Near Streets
-- Purpose: Identify streets with the highest number of nearby restaurants

-- Requirements:
-- - Use roads for street features
-- - Use pois for point features
-- - Filter POIs where fclass = 'restaurant'
-- - Use ST_DWithin to find restaurants within 0.25 miles (402 meters) of streets
-- - Use a CTE to isolate restaurant locations
-- - Count the number of restaurants near each street
-- - Exclude streets with no name (optional but recommended)
-- - Group by street name and geometry
-- - Order results by restaurant count (highest first)
-- - Include geom column for spatial visualization in GeoPandas

-- Expected Output:
-- - street_name
-- - nearby_restaurant_count
-- - geom

WITH restaurants AS (
    SELECT
        geom
    FROM
        pois
    WHERE
        fclass = 'restaurant'
)

SELECT
    rds.name AS street_name,
    COUNT(*) AS nearby_restaurant_count,
    rds.geom
FROM
    roads AS rds
JOIN
    restaurants AS r ON ST_DWithin(r.geom::geography, rds.geom::geography, 402)
WHERE
    rds.name IS NOT NULL
    AND rds.fclass = 'cycleway'
GROUP BY
    rds.name, rds.geom
ORDER BY
    nearby_restaurant_count DESC;