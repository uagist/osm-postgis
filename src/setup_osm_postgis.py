"""
OSM PostGIS Setup Workflow - Student Implementation

Complete the function in this file.
Use the notebook to build and run the workflow.

📋 FUNCTION TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function: setup_postgis_osm() → notebooks/setup_osm_postgis.ipynb
"""

import os
import psycopg2
import requests
import subprocess
import zipfile
from pathlib import Path
from typing import Optional

# Function: Setup PostGIS + Load OSM Shapefile Data

def setup_postgis_osm(
    osm_url: str,
    db_name: str = "osm_db",
    user: str = "postgres",
    password: str = "postgres",
    host: str = "localhost",
    port: int = 5432,
    data_dir: Optional[Path] = None
) -> None:
    """
    Create a PostGIS database and load Geofabrik shapefile data.

    This function performs a complete workflow:
    - Connect to PostgreSQL
    - Create a new database
    - Enable PostGIS extension
    - Download shapefile data from Geofabrik
    - Unzip shapefile data
    - Load shapefiles into PostGIS using shp2pgsql

    Args:
        osm_url: URL to Geofabrik shapefile ZIP
        db_name: Name of the database to create
        user: PostgreSQL username
        password: PostgreSQL password
        host: Database host
        port: Database port
        data_dir: Directory to store downloaded OSM data

    Returns:
        None

    Example:
        >>> setup_postgis_osm(
        ...     osm_url="https://download.geofabrik.de/north-america/us/hawaii-latest-free.shp.zip", db_name="hawaii"
        ... )
    """

    # TODO: Implement this function
    # Step 1: Setup data directory
    # Step 2: Download shapefile ZIP data
    # Step 3: Connect to PostgreSQL (default database)
    # Step 4: Create the working database
    # Step 5: Connect to the new database
    # Step 6: Enable PostGIS
    # Step 7: Unzip shapefile data
    # Step 8: Load shapefiles into PostGIS using shp2pgsql
    # Step 9: Close connections

    raise NotImplementedError("setup_postgis_osm not yet implemented")
