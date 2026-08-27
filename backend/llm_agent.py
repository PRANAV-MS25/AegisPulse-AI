import json

def synthesize_threat_advisory(target_data: dict) -> dict:
    """
    Generates a structured tactical assessment for elevated threats (YELLOW/RED).
    """
    callsign = target_data.get("callsign", "UNKNOWN")
    threat = target_data.get("threat", "GREEN")
    squawk = target_data.get("squawk", "NONE")
    alt = target_data.get("alt_m", 0)
    speed = target_data.get("speed_m_s", 0)
    rng = target_data.get("range_km", 0)
    bearing = target_data.get("bearing_deg", 0)
    reason = target_data.get("reason", "")

    # Structured threat analysis response
    if threat == "RED":
        action_plan = f"IMMEDIATE ACTION: Dispatch QRA interceptors on vector {bearing}°. Alert VOBL ATC."
        severity = "CRITICAL"
        assessment = f"Aircraft {callsign} transmitted EMERGENCY SQUAWK {squawk} at range {rng} km. High vulnerability risk."
    elif threat == "YELLOW":
        action_plan = f"MONITOR & CHALLENGE: Request secondary radar identification on bearing {bearing}°."
        severity = "ELEVATED"
        assessment = f"Unusual flight profile: Low altitude ({alt}m) with high velocity vector ({speed} m/s)."
    else:
        action_plan = "CONTINUE NOMINAL TRACKING."
        severity = "LOW"
        assessment = "Standard commercial flight corridor transit."

    return {
        "callsign": callsign,
        "threat_level": threat,
        "severity": severity,
        "assessment": assessment,
        "recommended_action": action_plan,
        "timestamp_utc": "REALTIME_SWEEP"
    }