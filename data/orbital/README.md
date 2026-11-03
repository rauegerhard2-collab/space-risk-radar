# Orbital data archive

The archive now separates orbital elements from catalogue enrichment:

- **CelesTrak STATIONS:** daily CCSDS OMM JSON snapshot, stored unchanged under `snapshots/` plus `latest.json`. This is a limited station group, not a global catalogue.
- **OrbitalWiki events:** optional daily catalogue-change snapshot under `orbitalwiki-events/`. Events are catalogue changes, not conjunction warnings or manoeuvres.
- **OrbitalWiki launches:** optional daily launch metadata snapshot under `orbitalwiki-launches/`. Launch records are not orbital ephemerides.

Each successful file includes source URL, UTC retrieval time and attribution. The source log records success or optional-feed failure. CelesTrak is required: if it fails or returns malformed data, the workflow stops without replacing the primary snapshot. OrbitalWiki is optional: an unavailable feed is logged and does not discard a valid CelesTrak snapshot.

OrbitalWiki's orbital elements are sourced from CelesTrak, so the project intentionally does not ingest its `/elements` endpoint as a second orbital feed. Its API is early access; payloads are preserved as returned, and schema changes may require code updates. ODbL-1.0 attribution is retained; upstream sources retain their own terms.

Orbital Watch Collision Watch is currently a public human-readable CDM reference, not an automated feed. The project does not scrape its HTML. No orbital-element snapshot by itself is a collision warning, collision probability or evidence of an executed avoidance manoeuvre.

The updater runs once daily at 07:17 UTC and can be started manually. It follows the branch on which the workflow was dispatched; it no longer pushes to the retired `feature/dashboard-v1-1` branch.
