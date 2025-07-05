#!/usr/bin/env python3
import pandas as pd
import geopandas as gpd
import os
from shapely.geometry import Point

INPUT_CSV      = "/Users/colehuetten/Projects/palntir/Wildlife-Grid-Navigator/data/Substations.csv"
CLEANED_ASSETS = "data/clean_assets.geojson"

def process_assets_from_csv(input_csv=INPUT_CSV, output_geojson=CLEANED_ASSETS):
    print(f"Reading CSV from {input_csv}")
    df = pd.read_csv(input_csv)

    df = df.dropna(subset=["LONGITUDE", "LATITUDE"])
    df["asset_id"] = df["OBJECTID"]
    df["geometry"] = df.apply(lambda r: Point(r["LONGITUDE"], r["LATITUDE"]), axis=1)

    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    # (Optional) drop unused columns to slim down the GeoJSON
    keep = ["asset_id", "NAME", "STATE", "COUNTY", "MAX_VOLT", "MIN_VOLT", "geometry"]
    gdf = gdf[keep]

    # Write out
    os.makedirs(os.path.dirname(output_geojson), exist_ok=True)
    gdf.to_file(output_geojson, driver="GeoJSON")
    print(f"Wrote {len(gdf)} assets to {output_geojson}")
    return gdf

if __name__ == "__main__":
    process_assets_from_csv()