import sqlite3
from datetime import datetime

DB_PATH = "incidents.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS threat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            callsign TEXT,
            squawk TEXT,
            threat_level TEXT,
            range_km REAL,
            bearing_deg REAL,
            advisory TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_incident(target: dict, advisory: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO threat_logs (timestamp, callsign, squawk, threat_level, range_km, bearing_deg, advisory)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.utcnow().isoformat(),
        target.get("callsign"),
        target.get("squawk"),
        target.get("threat"),
        target.get("range_km"),
        target.get("bearing_deg"),
        advisory
    ))
    conn.commit()
    conn.close()