import geopandas as gpd
import pandas as pd
import os

ASSETS_GEOJSON = "data/clean_assets.geojson"
BLOCKS_SHP    = "data/census_blocks.shp"  
OUTPUT_GEOJSON = "data/assets_with_population.geojson"

BUFFER_DISTANCE = 1000  

def calculate_population(
    assets_geojson=ASSETS_GEOJSON,
    blocks_shp=BLOCKS_SHP,
    out_geojson=OUTPUT_GEOJSON,
    buffer_dist=BUFFER_DISTANCE,
):
    assets = gpd.read_file(assets_geojson)
    blocks = gpd.read_file(blocks_shp)

    blocks = blocks.to_crs(assets.crs)

    assets["buffer_geom"] = assets.geometry.buffer(buffer_dist)

    joined = gpd.sjoin(
        blocks.set_geometry("geometry"), 
        assets.set_geometry("buffer_geom"), 
        how="inner", 
        predicate="intersects"
    )

    pop_by_asset = (
        joined.groupby("asset_id")["POP100"]
        .sum()
        .reset_index()
        .rename(columns={"POP100": "buffer_population"})
    )

    assets = assets.merge(pop_by_asset, on="asset_id", how="left")
    assets["buffer_population"] = assets["buffer_population"].fillna(0)

    assets = assets.drop(columns=["buffer_geom"])
    os.makedirs(os.path.dirname(out_geojson), exist_ok=True)
    assets.to_file(out_geojson, driver="GeoJSON")
    print(f"Assets with population saved to {out_geojson}")
    return assets

if __name__ == "__main__":
    calculate_population()