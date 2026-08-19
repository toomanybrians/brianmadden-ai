# sources/ — feed registry

`sources.yaml` is the list of feeds (RSS, YouTube, podcasts, Substacks,
people) the ingest skill polls to produce `ingest/` notes. Seeded from
[me/links.md](../me/links.md), which remains the human-readable version of
"what Brian reads."

Adding a source here does not make it canon — it only means the ingest skill
will read it and write quarantined notes to `ingest/`. Nothing here is
indexed for consuming AIs.

## Per-source lens

Two optional fields, `lens` (short tag) and `pov` (longer freeform text),
record Brian's personal read of a source — some he wants dissenting takes
from, some are must-follow, some are usually wrong but occasionally worth a
nugget. Both are blank-safe: an unset source is treated neutrally. When set,
`pov` is fed to the ingest skill's extraction prompt as framing instruction
(e.g. "surface where he disagrees with consensus"). Most sources don't have
either field yet — Brian expects to fill these in over time, not all at
once. See `sources.yaml`'s header comment for the full field list.
