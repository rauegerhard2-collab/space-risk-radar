#!/usr/bin/env python3
"""Fetch conservative public orbital snapshots with per-source provenance.

CelesTrak STATIONS OMM is the required pilot feed. OrbitalWiki's public
catalogue-events and launches endpoints are optional enrichment feeds.
OrbitalWiki's elements endpoint is intentionally not fetched because it
repackages CelesTrak elements and would duplicate the primary orbital feed.
"""
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "SpaceRiskRadar/0.2 (public research; source attribution in repository)"
CELESTRAK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=STATIONS&FORMAT=JSON"
OPTIONAL_FEEDS = {
    "orbitalwiki-events": "https://www.orbitalwiki.com/api/v1/events",
    "orbitalwiki-launches": "https://www.orbitalwiki.com/api/v1/launches",
}
REQUIRED_OMM = (
    "OBJECT_NAME", "OBJECT_ID", "EPOCH", "MEAN_MOTION", "ECCENTRICITY",
    "INCLINATION", "RA_OF_ASC_NODE", "ARG_OF_PERICENTER", "MEAN_ANOMALY",
)

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, (dict, list)) or not payload:
        raise ValueError("Unexpected or empty JSON payload")
    return payload

def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def append_log(entry):
    path = ROOT / "data/source-log.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as log:
        log.write(json.dumps(entry, ensure_ascii=False) + "\n")

def main():
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y-%m-%d")
    retrieved_at = now.isoformat(timespec="seconds")

    # Required primary feed: fail closed if this source is unavailable or malformed.
    try:
        stations = fetch_json(CELESTRAK_URL)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"CelesTrak fetch failed; no data was changed: {exc}")
    if not isinstance(stations, list) or not stations:
        raise SystemExit("CelesTrak response is not a non-empty OMM list; no data was changed.")
    for obj in stations:
        if not isinstance(obj, dict) or any(key not in obj for key in REQUIRED_OMM):
            raise SystemExit("CelesTrak OMM record is invalid; no data was changed.")

    snapshot = {
        "dataset_id": f"celestrak-stations-{stamp}",
        "retrieved_at": retrieved_at,
        "reference": "OMM epoch is per object; see each EPOCH field",
        "source": {
            "name": "CelesTrak General Perturbations (GP) API",
            "url": CELESTRAK_URL,
            "format": "CCSDS OMM JSON",
            "group": "STATIONS",
            "attribution": "Orbital elements provided by CelesTrak; source must be credited.",
        },
        "record_count": len(stations),
        "objects": stations,
    }
    orbital_dir = ROOT / "data/orbital"
    write_json(orbital_dir / "snapshots" / f"{stamp}.json", snapshot)
    write_json(orbital_dir / "latest.json", snapshot)
    append_log({
        "retrieved_at": retrieved_at, "source": "CelesTrak GP API",
        "dataset": "STATIONS", "record_count": len(stations),
        "status": "success", "url": CELESTRAK_URL,
    })
    print(f"Archived {len(stations)} CelesTrak STATIONS OMM records.")

    # Optional complementary metadata/event feeds. Their failure is recorded,
    # but does not invalidate the required CelesTrak snapshot.
    for dataset, url in OPTIONAL_FEEDS.items():
        try:
            payload = fetch_json(url)
            envelope = {
                "dataset_id": f"{dataset}-{stamp}",
                "retrieved_at": retrieved_at,
                "source": {
                    "name": "OrbitalWiki public read-only API",
                    "url": url,
                    "attribution": "OrbitalWiki; catalogue data under ODbL-1.0. Upstream sources retain their own terms.",
                },
                "record_type": (
                    "catalogue change events; not conjunction warnings or manoeuvre records"
                    if dataset.endswith("events")
                    else "launch catalogue metadata; not orbital ephemerides"
                ),
                "payload": payload,
            }
            folder = orbital_dir / dataset
            write_json(folder / "snapshots" / f"{stamp}.json", envelope)
            write_json(folder / "latest.json", envelope)
            count = len(payload) if isinstance(payload, list) else len(payload.get("data", [])) if isinstance(payload.get("data"), list) else None
            append_log({
                "retrieved_at": retrieved_at, "source": "OrbitalWiki API",
                "dataset": dataset, "record_count": count,
                "status": "success", "url": url,
                "note": "Complementary catalogue metadata; not an independent orbital-element or collision-warning feed.",
            })
            print(f"Archived OrbitalWiki {dataset} feed.")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            append_log({
                "retrieved_at": retrieved_at, "source": "OrbitalWiki API",
                "dataset": dataset, "record_count": None,
                "status": "failed_optional", "url": url, "error": str(exc),
            })
            print(f"WARNING: optional OrbitalWiki feed {dataset} unavailable: {exc}")

if __name__ == "__main__":
    main()
