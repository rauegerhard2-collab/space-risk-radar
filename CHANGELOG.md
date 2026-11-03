# Changelog

## 1.1.0-preview — 2026-11-03

- Introduced redesigned responsive dashboard preview.
- Added schematic orbital-environment illustration with explicit non-live disclaimer.
- Added interactive chart selector for catalogued and modelled population snapshots.
- Added collision-warning / risk-assessment / manoeuvre distinction.
- Added source and data-quality section.
- Added structured ESA metric snapshot baseline in `data/metrics.json`.
- Documented the 47,280 headline versus 47,290 detailed-table discrepancy in ESA's portal.
- Added project data-source and methodology notes.
- Kept development on `feature/dashboard-v1-1`; public `main` branch not changed.

## 1.2.0-dev — data pipeline foundation — 2026-11-03

- Added automatic HTML/metric integrity checks and a GitHub Actions validation workflow.
- Added a JSON Schema for curated metric snapshots.
- Added an append-only historical-data policy and initial dated metric snapshot.
- Added a machine-readable source retrieval log.
- Added a conservative daily CelesTrak STATIONS OMM ingestion workflow with date-stamped archives and failure-safe validation.
- Assessed CelesTrak, ESA DISCOSweb and Space-Track access, cadence, attribution and limitations.
- Kept all changes on `feature/dashboard-v1-1`; public `main` remains unchanged.

## Planned next

- Validate HTML and JSON automatically.
- Add a reproducible data-update workflow and source retrieval log.
- Introduce historical snapshot storage without fabricating missing months.
- Evaluate authoritative orbital element and event data feeds, licensing, terms of use and update cadence before integrating any live map or automated ingestion.
