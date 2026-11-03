# Historical data policy

- Preserve every successful retrieval as a date-stamped snapshot; never silently replace prior snapshots.
- Keep the source's original epoch/reference date separate from the retrieval timestamp.
- Store source name, exact endpoint, format, group/filter, record count and verification status.
- A failed or empty fetch must not overwrite the latest successful snapshot.
- Do not interpolate missing dates, fabricate monthly values, or treat daily retrievals as independent observations if the source data did not change.
- For the curated ESA metric series, add a point only when a source publishes a value with a defensible definition and reference date.
- If a source revises a historical figure, preserve the earlier value and record the revision as a new source snapshot with an explanation.
- Deduplication must use stable object/event identifiers plus source provenance; names alone are not reliable identifiers.
