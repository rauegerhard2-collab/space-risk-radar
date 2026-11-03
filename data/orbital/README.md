# Orbital data archive

The first automated orbital dataset is deliberately limited to CelesTrak's **STATIONS** group. It is a manageable, clearly defined sample for validating OMM ingestion and historical archiving; it is not a complete catalogue or a representative sample of all orbital traffic.

- Source: https://celestrak.org/NORAD/documentation/gp-data-formats.php
- Endpoint: CelesTrak GP API, GROUP=STATIONS, FORMAT=JSON
- Format: CCSDS Orbit Mean-Elements Message (OMM) JSON
- Schedule: once daily at 07:17 UTC, with manual workflow dispatch available
- Archive: one immutable date-stamped file per successful run under `snapshots/`
- Latest copy: `latest.json`
- Provenance: each file records retrieval time, source URL, group, record count and per-object OMM epoch

The archive records orbital elements, not collision warnings. It does not compute conjunction probabilities or avoidance manoeuvres. OMM epochs are object-specific and must be checked before any propagation. A future map must label its data time and freshness, and must not call this limited station group a live global picture.

The updater makes one request per scheduled run. It stops on HTTP errors, empty responses or missing required fields; it does not overwrite data with an invalid response.
