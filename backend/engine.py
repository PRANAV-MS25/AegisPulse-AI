import math
import requests

RADAR_CENTER = {"lat": 12.9716, "lon": 77.5946, "name": "VOBL Ground Radar"}
OPENSKY_URL = "https://opensky-network.org/api/states/all"

def haversine_polar(lat0, lon0, latt, lont):
    R = 6371.0 # Earth radius in km
    dlat = math.radians(latt - lat0)
    dlon = math.radians(lont - lon0)
    
    a = (math.sin(dlat / 2)**2 + 
         math.cos(math.radians(lat0)) * math.cos(math.radians(latt)) * math.sin(dlon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = R * c

    y = math.sin(dlon) * math.cos(math.radians(latt))
    x = (math.cos(math.radians(lat0)) * math.sin(math.radians(latt)) - 
         math.sin(math.radians(lat0)) * math.cos(math.radians(latt)) * math.cos(dlon))
    bearing_deg = (math.degrees(math.atan2(y, x)) + 360) % 360

    return round(distance_km, 2), round(bearing_deg, 2)

def fetch_live_targets(max_range_km=300):
    bbox = (RADAR_CENTER["lat"] - 3, RADAR_CENTER["lat"] + 3,
            RADAR_CENTER["lon"] - 3, RADAR_CENTER["lon"] + 3)
    params = {"lamin": bbox[0], "lamax": bbox[1], "lomin": bbox[2], "lomax": bbox[3]}
    
    try:
        res = requests.get(OPENSKY_URL, params=params, timeout=5)
        if res.status_code != 200: return []
        states = res.json().get("states", []) or []
    except Exception:
        return []

    processed = []
    for s in states:
        icao, callsign, lat, lon, alt, speed, squawk = s[0], s[1], s[6], s[5], s[7], s[9], s[14]
        if lat is None or lon is None: continue
        
        r, theta = haversine_polar(RADAR_CENTER["lat"], RADAR_CENTER["lon"], lat, lon)
        if r > max_range_km: continue

        threat = "GREEN"
        reason = "Nominal Airspace Transit"
        
        if squawk in ["7700", "7600", "7500"]:
            threat = "RED"
            reason = f"CRITICAL SQUAWK {squawk}"
        elif alt and alt < 600 and (speed or 0) > 220:
            threat = "YELLOW"
            reason = "Low Altitude High Velocity Vector"

        processed.append({
            "icao": icao,
            "callsign": callsign.strip() if callsign else "UNASSIGNED",
            "range_km": r,
            "bearing_deg": theta,
            "alt_m": alt,
            "speed_m_s": speed,
            "squawk": squawk,
            "threat": threat,
            "reason": reason
        })
    return processed