# LocalShout research dig — OpenActive is the quiet back door

Date: 2026-09-22

## The live-project question

LocalShout keeps pulling me toward Instagram, posters, venue pages, and brittle scraping because that is where the messy community-event surface is visible. The question for this dig was narrower: is there already a machine-readable events substrate nearby that LocalShout should exploit before building another scraper?

## Short answer

Yes — but it is not the generic “events API” layer I would have expected.

The surprising seam is **OpenActive**: a decentralised UK opportunity/event data ecosystem for sport and physical activity. It is not a full community-events feed, but it is real, standardised, live enough to have government standards attention, and close enough to LocalShout’s “what can I do near me?” shape that it deserves a spike.

## Evidence gathered

### 1. OpenActive has scale, not just a spec

A 2026 GOV.UK Data Standards Authority peer-review minute says OpenActive has been funded by Sport England since 2016 and standardises sport/physical-activity opportunity data from booking systems. It names the core specs as the modelling opportunity specification, RPDE transfer protocol, open booking API, and routes specification, and gives the useful scale marker: **approximately 10m activities and ~4,000 providers at any one time**.

Source: https://www.gov.uk/government/publications/meeting-minutes-for-the-data-standards-authority-governance-boards/dsa-peer-review-group-minutes-friday-30-january-2026-html

### 2. The data model is decentralised, which fits LocalShout better than one giant API

The `openactive` package documentation explains that there is no single owner or database. Publishers expose separate RPDE feeds; feeds are grouped into datasets, datasets into catalogues, and catalogues into one collection. That matches the LocalShout ingestion problem better than pretending there will be one canonical events provider.

Live fetch on 2026-09-22 found the OpenActive collection contains **5 catalogue URLs** in `hasPart`:

- `https://opendata.leisurecloud.live/api/datacatalog`
- `https://openactivedatacatalog.legendonlineservices.co.uk/api/DataCatalog`
- `https://openactive.io/data-catalogs/singular.jsonld`
- `https://app.bookteq.com/api/openactive/catalogue`
- `https://admin.rinktix.com/api/openactive/catalogue`

The singular catalogue contains **23 dataset URLs**, including Better, Let’s Ride, British Orienteering, British Triathlon, England Netball, GoodGym, OpenSessions, Our Parks, Playwaze, RunTogether, Sportsuite, and FindMyFacility.

Sources:
- https://libraries.io/pypi/openactive
- https://openactive.io/data-catalogs/data-catalog-collection.jsonld
- https://openactive.io/data-catalogs/singular.jsonld

### 3. Locaria is already building the “LocalShout-adjacent” version

Locaria describes a portal that can search events locally or nationally, filter by requirements like cost/date/skill/exertion/gender, add missing events, scan posters to create events, import events from URLs, moderate/edit before publishing, bookmark/share, publish by API, and view events in multiple languages.

Its data engine supports OpenActive RPDE feeds, polygon/area localisation, geospatial queries, complex filters, translation, and ML categorisation of posters/images/URLs.

That is uncomfortably close to the ingestion half of LocalShout. Not the community/product layer necessarily, but enough to treat as a reference implementation rather than an unknown.

Source: https://locaria.org/about

### 4. Eventbrite is not the obvious base layer anymore

Eventbrite still advertises platform capabilities around public events, but its own “Searching Events by Date” documentation says the Event Search API access was shut down at 11:59pm PT on 12 Dec 2019. That does not mean Eventbrite is unusable, but it does mean “just use Eventbrite search” is a stale assumption for LocalShout-style broad discovery.

Source: https://www.eventbrite.com/platform/docs/by-date

### 5. The old community-calendar problem has not gone away

An Open Knowledge Forum thread from the open-data community is still painfully relevant: Google Calendar is easy until write access deletes things, recurring events lie forever, filters are weak, timezone handling matters, and imported data still needs curation. The line that matters for LocalShout: an aggregator cannot safely treat imported events as truth without some expiry/review/custody model.

Source: https://discuss.okfn.org/t/community-event-api-where-are-you/7444

## What surprised me

The surprise was not “there is an events standard”. The surprise was that the closest useful substrate is **not general culture/events** but **sport/activity opportunities** — exactly the category where locality, recurrence, booking availability, provider identity, and stale-data risk are hardest to fake.

That makes OpenActive a better test bed than concerts or festivals. If LocalShout can ingest activity opportunities with provenance, expiry, dedupe, and venue normalisation, it has learned the hard shape before touching Instagram chaos.

## Recommendation

Do a two-day LocalShout spike called **activity-feed custody**:

1. Pick one bounded geography: Watford + a London control area.
2. Harvest a small slice from OpenActive catalogues/datasets.
3. Store each imported event with explicit custody fields:
   - source URL
   - publisher/provider
   - feed/catalogue
   - fetched_at
   - event start/end
   - recurrence/series relationship if present
   - expiry/review rule
4. Render a LocalShout admin page that marks each item as source-backed, stale-risk, duplicate-risk, or needs-human-review.
5. Compare against Locaria’s stated feature set so LocalShout’s differentiated layer is clear.

Do **not** start with “scrape every venue page”. Start with a standardised, live-ish feed where the ingestion contract is visible. Then use posters/Instagram as a supplement for the bits OpenActive cannot cover.

## Source matrix

| Source | What it proves | LocalShout implication |
|---|---|---|
| GOV.UK DSA minutes | OpenActive has government standards attention and reported scale | Treat it as infrastructure, not a hobby spec |
| OpenActive catalogues | Data is decentralised through catalogues/datasets/feeds | Build ingestion around source custody, not one provider |
| Locaria | Someone is already combining OpenActive, URL import, poster OCR, geospatial filtering | Use as reference/competitor for ingestion workflow |
| Eventbrite docs | Public event search API shutdown warning remains in docs | Avoid betting discovery on Eventbrite search |
| OKFN thread | Calendar aggregation fails on deletion, recurrence, filters, stale truth | Every import needs expiry/review semantics |
