# Space Risk Radar

Independent public information project for understanding the orbital environment.

**Live site:** https://rauegerhard2-collab.github.io/space-risk-radar/  
**Repository:** https://github.com/rauegerhard2-collab/space-risk-radar

## Project status

The approved public-information dashboard is published from main. It is not an operational collision-warning service. Maintained public-source data are retrieved daily into an isolated staging branch and published only after weekly validation.
## Scope

- Publicly documented orbital-environment indicators
- Catalogue snapshots and modelled debris-population estimates
- Fragmentation and re-entry context
- Public collision-avoidance information, where evidence is available
- Source transparency, data quality labels and explicit gaps

The first release is intentionally neutral and independent. It does not represent Deutsche Telekom AG, ESA, or any other organization.

## Data principles

1. Keep observed/catalogued values separate from modelled estimates.
2. Preserve each source's reference date and definition.
3. Do not interpolate missing months or manufacture event records.
4. Distinguish conjunction warnings, operator risk assessments and executed avoidance manoeuvres.
5. Record source URLs and retrieval dates for every maintained dataset.
6. Make uncertainty and known coverage gaps visible.

## Repository layout (target)

- `index.html` — dashboard interface
- `data/metrics.json` and `data/history/` — curated metric baseline and dated history
- `data/orbital/` — date-stamped CelesTrak OMM snapshots (STATIONS pilot)
- `data/source-log.jsonl` — machine-readable retrieval log
- `scripts/` — validation and data ingestion scripts
- `.github/workflows/` — automated validation and scheduled retrieval
- `docs/` — source register, feed assessment and historical-data policy
- `CHANGELOG.md` — project changes

## Current data limitation

ESA's Space Debris User Portal summary currently reports approximately 47,280 catalogued objects (updated 2 November 2026). Its detailed object-by-orbit table displays a total of 47,290. This 10-object difference is preserved as a source discrepancy and must not be silently reconciled. The dashboard uses the portal's headline summary and flags the detailed-table difference in the structured data record.

ESA's MASTER-8 reference population (February 2026) estimates 68,450 objects larger than 10 cm, approximately 1.5 million objects from greater than 1 cm to 10 cm, and approximately 230 million from greater than 1 mm to 1 cm. These are model estimates, not catalogue counts.

## Automated data retrieval

The production pipeline retrieves CelesTrak ACTIVE and STATIONS data plus OrbitalWiki event and launch metadata daily into the isolated data-staging branch. A weekly publication workflow checks all four feeds for freshness, valid JSON structure, matching retrieval timestamps and consistent record counts before copying only the data files to main. Failed or stale feeds block publication and preserve their last-known-good snapshots.

The footer's data date is populated from the actual ACTIVE snapshot retrieval time. The “Status aktualisieren” button reloads the published source log only; it does not start a new retrieval. ESA public statistics remain manually verified according to the provider's publication cadence, and the Orbital Radar embed is externally maintained.

See docs/AUTOMATED_DATA_REFRESH.md, data/orbital/README.md and docs/VALIDATION.md.

## Development

Changes are developed on feature branches. The public site is updated only after review and an explicit release decision.
