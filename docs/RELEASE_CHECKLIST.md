# Release readiness checklist — Space Risk Radar v1.2

Last reviewed: 3 November 2026

This checklist governs the proposed v1.2 release from `feature/dashboard-v1-2-interactions` to `main`. A successful data-ingestion run alone is not release approval. The public v1.1 site remains the production version until the maintainer explicitly approves and merges the pull request.

## Release gates

### 1. Source and licence review
- [x] CelesTrak STATIONS OMM source documented; retrieval time and per-object epoch retained.
- [x] OrbitalWiki events and launches documented as optional catalogue enrichment, not independent orbital surveillance.
- [x] Orbital Watch Collision Watch documented as a human-reviewed reference only; no unsupported HTML scraping.
- [x] SatNOGS DB identified as a possible read-only radio/transmitter metadata source under CC BY-SA; integration remains blocked pending bounded API/pagination/schema test.
- [ ] Space-Track account, terms, rate limits, CDM access and redistribution permissions reviewed before any direct integration.
- [ ] ESA DISCOSweb account and current redistribution/attribution terms reviewed before automation.

### 2. Data quality and provenance
- [x] Automated updater validates non-empty CelesTrak OMM records and required fields.
- [x] Optional OrbitalWiki failures are logged without discarding a valid primary snapshot.
- [x] Source log records UTC retrieval time, source, dataset, record count and status.
- [x] Dashboard source-health panel reads the source log and warns on stale feeds.
- [ ] Verify source-health panel in a real browser at desktop and mobile widths.
- [ ] Confirm stale, failed, missing-log and malformed-log states behave clearly.
- [ ] Confirm all visible statistics retain the distinction between catalogue, modelled, derived and reported values.
- [ ] Confirm every chart has a stated reference period and does not imply missing observations are zero.

### 3. Functional and accessibility checks
- [x] Interactive controls have keyboard focus treatment and keyboard activation.
- [x] Dialog supports Escape close; reduced-motion styling is present.
- [ ] Manual browser test of all KPI cards, chart points, timeline entries, orbit-layer toggles and detail dialogs.
- [ ] Manual keyboard-only pass and screen-reader spot check of labels, focus order and dialog announcement.
- [ ] Check responsive layout at desktop, tablet and mobile sizes.
- [ ] Check browser console for JavaScript errors and failed network requests.

### 4. Build, workflow and publication
- [x] Orbital snapshot workflow integration test succeeded for CelesTrak, OrbitalWiki events and launches.
- [x] CI validation succeeded for the source-code change commit.
- [ ] Re-run/resolve PR validation for the final head commit; investigate any `action_required` state.
- [ ] Review complete PR diff and verify no credentials, tokens or private data are present.
- [ ] Mark PR ready for review only after the preceding checks pass.
- [ ] Maintainer explicitly approves and merges PR #2.
- [ ] Verify GitHub Pages deployment and smoke-test the public v1.2 URL after merge.
- [ ] Keep a rollback path to the previous known-good deployment.

## Data-source test currently passed

The GitHub Actions integration run on 3 November 2026 retrieved:
- CelesTrak GP API / STATIONS: 20 OMM records.
- OrbitalWiki events: 100 returned records.
- OrbitalWiki launches: 1,998 returned records.

These counts describe that individual retrieval, not a guarantee of complete global coverage. OrbitalWiki's event endpoint returned 100 records in the test; this is not evidence that the endpoint exposes the complete event history.

## Publication rule

Version 1.2 may be published once all release gates marked `[ ]` are either completed or explicitly documented as accepted limitations, the PR is reviewed, and the maintainer gives explicit merge approval. Until then, the existing public v1.1 remains unchanged.

The dashboard is an independent public information project, not an operational collision-warning service and not affiliated with ESA or Deutsche Telekom AG.
