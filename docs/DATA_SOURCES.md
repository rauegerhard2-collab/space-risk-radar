# Data sources and interpretation

Last reviewed: 3 November 2026

## Primary source: ESA Space Debris User Portal

URL: https://sdup.esoc.esa.int/discosweb/statistics/  
Portal summary update: 2 November 2026

Headline indicators shown by the portal:
- About 47,280 objects regularly tracked and maintained in space-surveillance catalogues.
- More than 660 break-ups, explosions, collisions or anomalous events resulting in fragmentation.
- MASTER-8 reference population (02/2026): 68,450 objects larger than 10 cm, including approximately 11,300 active payloads.
- Approximately 1.5 million debris objects greater than 1 cm and up to 10 cm.
- Approximately 230 million debris objects greater than 1 mm and up to 1 cm.

### Source discrepancy

The same portal's detailed table, "Current number of orbiting objects per type and orbital regime", reports a total of 47,290, while the headline summary reports about 47,280. The dashboard currently displays the headline summary (47,280) and retains this discrepancy in the project data. Do not treat the two values as interchangeable or imply a precision that the portal itself does not provide.

### Interpretation

- "Catalogued" means objects whose orbital elements are maintained for prolonged periods in a space-surveillance catalogue.
- MASTER-8 population figures are statistical model estimates, not directly catalogued object counts.
- The 1–10 cm and 1 mm–1 cm populations are estimates, not individually observed inventories.
- "More than 660" is a cumulative count of events resulting in fragmentation, not an annual event rate.

## ESA Space Environment Report 2026

URL: https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2026  
Original report PDF: https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I10R0_20260501.pdf

The 2026 report is the tenth edition and was released on 1 May 2026. It describes the environment using data through the end of 2025 and includes model-based future-environment analysis. A report publication date must not be mistaken for a real-time data cut-off.

## Public conjunction information

Orbital Watch Collision Watch: https://orbitalwatch.app/collision-watch

This is a public information source for selected conjunction-related information. It is not a complete global record of all warnings, operator decisions or executed manoeuvres. Coverage, update times, event identity and definitions must be assessed before records are aggregated.

## Data labels

- **OBSERVED / CATALOGUED:** measured, tracked or listed in a surveillance catalogue. Include epoch, catalogue/source and definition.
- **MODELLED:** estimated from a statistical or physical model. Include model version, size threshold and reference population date.
- **DERIVED:** calculated from other values. Document formula, input records and uncertainty.
- **REPORTED:** an event or statement published by an identified source but not independently verified by this project.

## Minimum record fields for future ingestion

`metric_id`, `value`, `unit`, `classification`, `reference_date`, `published_date`, `retrieved_at`, `source_name`, `source_url`, `definition`, `uncertainty_note`, `verification_status`.

No missing month may be filled by interpolation unless a future analytical product explicitly labels such a transformation and explains its method. The default dashboard must show gaps as gaps.
