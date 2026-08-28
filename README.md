# 📡 AegisPulse-AI | Real-Time Tactical Airspace Radar & AI Threat Evaluator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Uvicorn-0.22+-499848?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn" />
  <img src="https://img.shields.io/badge/WebSockets-Live-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="WebSockets" />
  <img src="https://img.shields.io/badge/OpenSky%20Network-Live%20Telemetry-00599C?style=for-the-badge" alt="OpenSky" />
  <img src="https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge" alt="License" />
</p>

---

## 🚁 Overview

**AegisPulse-AI** is an intelligent, real-time tactical air radar monitoring system centered around **Kempegowda International Airport (VOBL Ground Radar, Bengaluru)**. It pulls live ADS-B telemetry from the OpenSky Network, converts geographical coordinates into polar vectors (range and bearing), and streams live targets across a WebSockets pipeline to an interactive HTML5 Tactical Sweep radar interface.

Integrated with a **Deterministic & LLM Tactical Threat Engine**, AegisPulse-AI dynamically categorizes airspace threats (`GREEN`, `YELLOW`, `RED`) based on emergency squawk codes (e.g., 7700/7600), altitude deltas, and velocity thresholds to deliver instant tactical advisory reports.

---

## ✨ Key Features

* **🛰️ Live ADS-B Tracking:** Streams active aircraft within a **300 km radius** of VOBL station using the OpenSky API.
* **⚡ High-Performance WebSockets Pipeline:** Async data pipeline pushing real-time position updates every 5 seconds.
* **🧭 Trigonometric Tactical Math:** Translates $Latitude/Longitude$ into $Range (km)$ and $Bearing (\degree)$ centered on radar coordinates.
* **🚨 Threat Assessment Engine:** Dynamic rule matching and AI threat advisory generation for emergency situations.
* **🖥️ Interactive HTML5 Radar UI:** Visual sweep interface rendering active blips, altitude vectors, callsigns, and alert banners.

---

## 🏗️ System Architecture

```text
       ┌────────────────────────┐
       │ OpenSky Network API    │
       │ (Live ADS-B Telemetry) │
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ AegisPulse Engine      │
       │  - Polar Vector Calc   │
       │  - Distance Filtering  │
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ Tactical Threat Engine │
       │  - Squawk 7700/7600    │
       │  - LLM Tactical Brief  │
       └───────────┬────────────┘
                   │ (WebSockets / JSON)
                   ▼
       ┌────────────────────────┐
       │ Interactive Frontend   │
       │  - Canvas Radar Sweep  │
       │  - Live Target Table   │
       └────────────────────────┘

 🚀 Quickstart & Setup Guide
1. Prerequisite Requirements
Python 3.10+

Git

2. Clone the Repository
Bash
git clone [https://github.com/PRANAV-MS25/AegisPulse-AI.git](https://github.com/PRANAV-MS25/AegisPulse-AI.git)
cd AegisPulse-AI
3. Create & Activate Virtual Environment
Windows (Command Prompt):

DOS
python -m venv venv
venv\Scripts\activate
macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
Bash
pip install -r requirements.txt
🏃 Running the Application
Start the FastAPI application with Uvicorn hot-reloading:

Bash
uvicorn backend.main:app --reload --port 8000
Access Points:
Tactical Radar UI: http://127.0.0.1:8000

WebSocket Endpoint: ws://127.0.0.1:8000/ws/radar

Interactive API Documentation: http://127.0.0.1:8000/docs

🛡️ License
Copyright (c) 2026 M Pranav. All Rights Reserved.

This repository and its contents are strictly proprietary. No part of this project may be reproduced, distributed, or modified without explicit written permission.

Push changes to GitHub
Run these terminal commands to send the updated README.md live to your repository:

DOS
git add README.md
git commit -m "docs: complete updated README with proprietary license badge and full setup guide"
git push
