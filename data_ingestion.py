import requests
import pandas as pd
import os

BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"


def fetch_earthquakes():
    params = {
        "format": "geojson",
        "starttime": "2023-01-01",
        "endtime": "2024-12-31",
        "minmagnitude": "1.5",
        "limit": "20000",
        "orderby": "time-asc",
    }

    print("Fetching earthquake data from USGS API...")
    response = requests.get(BASE_URL, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()

    features = data["features"]
    print(f"Fetched {len(features)} earthquake records.")

    records = []
    for f in features:
        props = f["properties"]
        coords = f["geometry"]["coordinates"]

        records.append({
            "id": f["id"],
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2],
            "mag": props.get("mag"),
            "magType": props.get("magType"),
            "nst": props.get("nst"),
            "gap": props.get("gap"),
            "dmin": props.get("dmin"),
            "rms": props.get("rms"),
            "place": props.get("place"),
            "type": props.get("type"),
            "status": props.get("status"),
            "time_ms": props.get("time"),
        })

    df = pd.DataFrame(records)

    # Parse time
    df["time"] = pd.to_datetime(df["time_ms"], unit="ms")
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month
    df.drop(columns=["time_ms", "time"], inplace=True)

    # Extract broad region from place string (e.g., "10km SE of City, CA" → "CA")
    df["region"] = df["place"].str.extract(r",\s*(.+)$")
    df["region"] = df["region"].fillna("Unknown")

    # Drop rows missing the dependent variable or key features
    df = df.dropna(subset=["mag", "depth", "magType"])

    print(f"Final dataset shape: {df.shape}")
    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = fetch_earthquakes()
    print(df.dtypes)
    print(df.head())
    out_path = os.path.join("data", "earthquakes.csv")
    df.to_csv(out_path, index=False)
    print(f"\nSaved to {out_path}")
