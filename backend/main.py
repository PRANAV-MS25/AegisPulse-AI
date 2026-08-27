import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

from backend.engine import fetch_live_targets, RADAR_CENTER
from backend.llm_agent import synthesize_threat_advisory

app = FastAPI(title="AegisPulse-AI Radar Backend")

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def get_index():
    with open(os.path.join(frontend_path, "index.html"), "r") as f:
        return HTMLResponse(content=f.read())

@app.websocket("/ws/radar")
async def radar_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Radar Client Connected to Live Feed.")
    try:
        while True:
            targets = fetch_live_targets(max_range_km=300)
            
            # Enrich targets with threat advisory evaluations
            enriched_targets = []
            for target in targets:
                if target["threat"] in ["YELLOW", "RED"]:
                    target["advisory"] = synthesize_threat_advisory(target)
                enriched_targets.append(target)
            
            payload = {
                "station": RADAR_CENTER["name"],
                "total_targets": len(enriched_targets),
                "targets": enriched_targets
            }
            
            await websocket.send_json(payload)
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print("Radar Client Disconnected.")
    except Exception as e:
        print(f"WebSocket Error: {e}")