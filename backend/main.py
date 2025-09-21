# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow requests from your frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # change to ["*"] only for quick testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Air Pollution API is running"}

@app.get("/pollution")
def get_pollution(city: str = "Delhi"):
    url = f"https://api.openaq.org/v2/latest?city={city}"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        payload = res.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Error fetching data: {e}")

    data = []
    for r in payload.get("results", []):
        coords = r.get("coordinates", {})
        lat = coords.get("latitude")
        lon = coords.get("longitude")
        if lat is None or lon is None:
            # skip stations without coordinates
            continue
        for m in r.get("measurements", []):
            data.append({
                "location": r.get("location"),
                "lat": lat,
                "lon": lon,
                "parameter": m.get("parameter"),
                "value": m.get("value"),
                "unit": m.get("unit"),
                "lastUpdated": m.get("lastUpdated"),
            })
    return data
