#!/usr/bin/env python3
"""Fetch one modest CelesTrak STATIONS OMM snapshot and archive it unchanged."""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=STATIONS&FORMAT=JSON"
REQUIRED = ("OBJECT_NAME", "OBJECT_ID", "EPOCH", "MEAN_MOTION", "ECCENTRICITY",
            "INCLINATION", "RA_OF_ASC_NODE", "ARG_OF_PERICENTER", "MEAN_ANOMALY")

def main():
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y-%m-%d")
    req = urllib.request.Request(URL, headers={"User-Agent": "SpaceRiskRadar/0.1 (public research; source attribution in repository)"})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            if response.status != 200:
                raise RuntimeError(f"CelesTrak returned HTTP {response.status}")
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Fetch failed; no data was changed: {exc}")
    if not isinstance(payload, list) or not payload:
        raise SystemExit("Unexpected/empty CelesTrak response; no data was changed.")
    missing = sorted({key for obj in payload if isinstance(obj, dict) for key in REQUIRED if key not in obj})
    if missing:
        raise SystemExit("OMM fields missing: " + ", ".join(missing))
    for obj in payload:
        if not isinstance(obj, dict) or any(k not in obj for k in REQUIRED):
            raise SystemExit("Invalid object record; no data was changed.")
    snapshot = {
        "dataset_id": f"celestrak-stations-{stamp}",
        "retrieved_at": now.isoformat(timespec="seconds"),
        "reference": "OMM epoch is per object; see each EPOCH field",
        "source": {"name": "CelesTrak General Perturbations (GP) API", "url": URL,
                   "format": "CCSDS OMM JSON", "group": "STATIONS",
                   "attribution": "Orbital elements provided by CelesTrak; source must be credited."},
        "record_count": len(payload),
        "objects": payload
    }
    outdir = ROOT / "data/orbital/snapshots"
    outdir.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    (outdir / f"{stamp}.json").write_text(encoded, encoding="utf-8")
    (ROOT / "data/orbital/latest.json").write_text(encoded, encoding="utf-8")
    log_path = ROOT / "data/source-log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log:
        log.write(json.dumps({"retrieved_at": snapshot["retrieved_at"], "source": "CelesTrak GP API",
                              "dataset": "STATIONS", "record_count": len(payload),
                              "status": "success", "url": URL}, ensure_ascii=False) + "\n")
    print(f"Archived {len(payload)} station-group OMM records for {stamp}.")

if __name__ == "__main__":
    main()
