# Orbital and event feed assessment

Reviewed: 3 November 2026

## CelesTrak GP API — selected for the first ingestion pilot

Official documentation: https://celestrak.org/NORAD/documentation/gp-data-formats.php  
Usage policy: https://celestrak.org/usage-policy.php

CelesTrak publishes general perturbations/orbital element sets in CCSDS OMM-compatible JSON, CSV, XML and KVN, alongside legacy TLE formats. OMM is the preferred format for forward compatibility with catalog numbers beyond five digits. The API supports curated groups, including STATIONS, and documents that data is checked/updated on a two-hour cycle. Its usage policy asks clients to retrieve only what they need and not poll more frequently than the update cadence.

**Decision:** begin with one daily STATIONS-group JSON retrieval. Preserve the source OMM records unchanged with a UTC retrieval timestamp and per-object epoch. Do not poll the full active catalogue, do not query every satellite individually, and stop on non-200 responses. This is an ingestion pilot, not an operational safety feed.

## ESA DISCOSweb — valuable metadata, access conditions to resolve

Official portal: https://discosweb.esoc.esa.int/

DISCOS provides reference information about launches, object registration, spacecraft characteristics and fragmentation context. ESA states that users register and accept the DISCOSweb terms; orbital/attitude ephemerides from surveillance systems are not distributed through DISCOSweb. ESA also requires source acknowledgement when data are used in derived works or redistributed.

**Decision:** use as a potential metadata enrichment source after account registration and review of current terms/API version. Do not treat it as a source of live orbital positions or conjunction warnings.

## Space-Track — authoritative but account-governed

Documentation: https://www.space-track.org/documentation

Space-Track provides API access to GP/OMM, catalogue, decay and conjunction data-message classes, with explicit rate limits and data retrieval rules. Its documentation gives separate limits for GP, CDM, SATCAT and other classes.

**Decision:** do not automate against it until a project-owned account, credentials handling, applicable terms, redistribution rights and intended CDM use have been reviewed. Credentials must never be committed to this public repository. Do not present CDMs as a complete public global record of operator decisions or manoeuvres.

## Collision-warning data limitations

Orbital elements alone are not collision warnings. A defensible conjunction product requires suitable ephemerides, covariance/uncertainty, close-approach time and distance, probability definition, screening coverage, object identity resolution and provenance. Operational warnings and executed manoeuvres may be restricted or unavailable publicly.

The project therefore keeps four layers separate:
1. Orbital element observations/catalogue records.
2. Derived propagated positions (with model, epoch and uncertainty).
3. Conjunction screening / warning messages.
4. Operator risk decisions and confirmed manoeuvres.

No layer may be inferred from another. A map based on a selected object group is not a global risk map.
