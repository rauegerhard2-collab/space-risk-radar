#!/usr/bin/env python3
"""Lightweight integrity checks for the public Space Risk Radar data files."""
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DashboardParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.title_seen = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
    def handle_data(self, data):
        if data.strip() == "SPACE RISK RADAR | Orbital Environment Intelligence":
            self.title_seen = True

def fail(message):
    raise SystemExit("VALIDATION ERROR: " + message)

def main():
    html_path = ROOT / "index.html"
    metrics_path = ROOT / "data/metrics.json"
    if not html_path.exists():
        fail("index.html missing")
    if not metrics_path.exists():
        fail("data/metrics.json missing")
    parser = DashboardParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    required_ids = {"overview", "orbital-map", "trends", "watch", "context", "sources"}
    missing = required_ids - parser.ids
    if missing:
        fail("dashboard sections missing: " + ", ".join(sorted(missing)))
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    if not isinstance(metrics.get("metrics"), list) or not metrics["metrics"]:
        fail("metrics.json must contain a non-empty metrics array")
    seen = set()
    for item in metrics["metrics"]:
        for key in ("id", "value", "unit", "classification", "reference_date", "source_url"):
            if key not in item:
                fail(f"metric missing {key}: {item.get('id', '<unknown>')}")
        if item["id"] in seen:
            fail("duplicate metric id: " + item["id"])
        seen.add(item["id"])
        if item["classification"] not in {"OBSERVED / CATALOGUED", "MODELLED", "DERIVED", "REPORTED"}:
            fail("unknown classification for " + item["id"])
        if not isinstance(item["value"], (int, float)):
            fail("non-numeric value for " + item["id"])
    if metrics.get("methodology", {}).get("no_interpolation") is not True:
        fail("no_interpolation must remain true")
    print(f"OK: dashboard sections, {len(metrics['metrics'])} metrics and methodology checks passed.")

if __name__ == "__main__":
    main()
