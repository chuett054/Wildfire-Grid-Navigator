import requests
import geopandas as gpd
import os

URL = (
    "https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services/"
    "WFIGS_Interagency_Perimeters_Current/FeatureServer/0/query"
    "?where=1=1"
    "&outFields=*"
    "&f=geojson"
)

OUT_DIR = "data"
OUT_FILE = os.path.join(OUT_DIR, "noaa_perimeters.geojson")

def fetch_and_save_geojson(url=URL, out_path=OUT_FILE):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    print(f"fetching NOAA data from {url} …")
    resp = requests.get(url)
    resp.raise_for_status()
    with open(out_path, "w") as f:
        f.write(resp.text)
    print(f"saved raw GeoJSON to {out_path}")
    gdf = gpd.read_file(out_path)
    print(f"Loaded {len(gdf)} features into GeoDataFrame")
    return gdf

if __name__ == "__main__":
    fetch_and_save_geojson()
