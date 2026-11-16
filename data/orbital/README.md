# Orbital data snapshots

The production main branch publishes a small, explicitly scoped set of current public snapshots:

- CelesTrak ACTIVE: provider-defined subset used to calculate approximate orbit-regime counts; not a complete object catalogue or collision-risk feed.
- CelesTrak STATIONS: selected station-group OMM records, not a global satellite/debris catalogue.
- OrbitalWiki events: recent catalogue-change metadata; its history is limited and is not a conjunction-warning or manoeuvre feed.
- OrbitalWiki launches: catalogue metadata derived from object designators; not orbital ephemerides.

Daily retrievals are committed to the isolated data-staging branch. A weekly quality gate copies only valid, recent snapshots and the source log to main. A failed feed is logged and cannot overwrite its last-known-good snapshot or be published as part of a partial weekly release.

Every snapshot carries a UTC retrieval timestamp distinct from provider-generated times and per-object OMM epochs. The source log records the actual retrieval time, record count and result for each maintained feed.

The existing dated archive and its earlier feature-branch ingestion pilot are retained as historical development material. They are not the publication mechanism for the production site.

These data are for public-information and situational-awareness context only. They are not operational conjunction assessments, collision warnings, confirmed avoidance manoeuvres or indicators of service impact.
