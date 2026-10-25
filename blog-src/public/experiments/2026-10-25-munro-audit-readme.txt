Munro section audit — 25 October 2026

Question: do the saved collection's SMC section assignments agree with the
source table named in the June design note (JIM-2765)?

Inputs, pinned rather than latest:
CSV:
https://raw.githubusercontent.com/debruine/30DCC-2022/dd1332e8318889559326ea86782f7209893ef3f8/data/munrotab_v8.0.1.csv
Collection:
https://raw.githubusercontent.com/marvinbarretto/collectr/78a674f6e6fb3e0e410b738e6392f5fc8f5d0970/data/munros/munros.json
Prototype comparison:
https://raw.githubusercontent.com/marvinbarretto/collectr/78a674f6e6fb3e0e410b738e6392f5fc8f5d0970/prototypes/region-collector-v5/data/munros.json

The collectr repository may require your existing GitHub access. No credentials
are included here. Download those inputs as source.csv and collection.json.
Download the audit and test beside one another, then run:

PYTHONDONTWRITEBYTECODE=1 python3 2026-10-25-munro-audit-test.py
python3 2026-10-25-munro-audit.py source.csv collection.json

Observed result for BOTH collection files:
282 source rows with 2021 == MUN; 282 collection rows and unique exported IDs;
282 unique source IDs matched, none reused, no unresolved candidates;
12 SMC section disagreements. Five regression tests passed.

Matching policy: source Name.strip() plus Python round(float(Height (m))),
compared to the exported name and height_m. A candidate count other than one
is unresolved, never silently chosen. This is a diagnostic witness only.
It does not establish that name+height is a safe durable identity scheme.

The saved result is output from the main data/munros input. The v5 output was
byte-identical. Inputs retrieved at HEAD were also compared byte-for-byte with
these pinned versions before publication.

Additional observation: all 12 mismatching sections equal the section in the
last current-Munro CSV row with the same trimmed name. This is consistent with
a last-write-wins name lookup. The original transformation was NOT recovered;
its implementation and root cause remain unverified.

Verdict: INVALIDATED for the proposition that unique exported IDs establish
source section fidelity. This is an audit of saved files, not a production
security check, geography certification, app test, or correction. No collection,
user check-in or production record was modified. Coordinates and county
boundaries were not validated. The historical table is not a freshly checked
statement of today's official Munro list.

The experiment uses Python stdlib unittest rather than the house Vitest
convention: it is a standalone, dependency-free downloadable Python diagnostic,
not application code. All writes are shell redirection of its read-only output.
