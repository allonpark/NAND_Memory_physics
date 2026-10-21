# Evidence Ledger (claims/)

This folder holds the machine-readable evidence ledger of the weekly reports. One JSON file per week
(`claims/<year>-w<week>.json`, for example `2026-w40.json`) plus `claims/index.json`.
Only the Python standard library is needed to read and check them: `python3 -I scripts/report_lint.py claims-validate`.

The ledger records what a source states and how strongly we may rely on it. It is not a summary of the report.
A statement that is only this report's own inference does not belong in a file here unless it is labeled as such.

## File layout

```json
{
  "schema_version": 1,
  "week": "2026-W40",
  "year": 2026,
  "provenance": { "built_from": "...", "method": "...", "not_covered": "..." },
  "sources": [ { "doi": "10.xxxx/...", "title": "...", "access": "abstract_only" } ],
  "claims":  [ { ...claim record... } ]
}
```

`claims/index.json` lists the files (`week`, `path`, `claims_count`), holds the `new_week_policy` marker
(see `docs/quality/README.md`) and an optional `allowed_duplicate_dois` list.

## Claim record

| field | type | rule |
|---|---|---|
| `id` | string | `YYYY-wWW-cNNN`, unique inside the file, never reused |
| `week` | string | `YYYY-Www`, must equal the file's week |
| `source.doi` | string | well-formed DOI that is also listed in `sources[]` |
| `source.location.kind` | enum | `abstract`, `figure`, `table`, `equation`, `text` |
| `source.location.ref` | string | free text, for example `Fig. 3b`, `Eq. 4`, `Table II` |
| `conditions` | object | keys `material`, `geometry`, `temperature`, `bias`, `time`, `sample_count` must all be present. A condition the source does not state is the literal string `"UNKNOWN"`. Never fill a gap from memory. |
| `quantity` | object or null | `name`, `unit`, and `value` or `value_min`/`value_max` (numbers); optional `comparator` (`approx`, `<=`, `>`, ...). `null` when the claim has no number. |
| `label` | enum | `SOURCE_REPORTED`, `AUTHOR_INTERPRETATION`, `ENGINEERING_INFERENCE`, `UNKNOWN`, `EXTRAPOLATION_ONLY` |
| `grade` | enum | `A`, `B`, `C`, `D` only. Suffixes such as `B-` are invalid. |
| `access` | enum | `full_text` or `abstract_only` |
| `status` | enum | `supported`, `contested`, `superseded` |
| `claim_type` | enum | `observation`, `quantity`, `method`, `mechanism`, `scope` |
| `text` | string | the claim wording. For `SOURCE_REPORTED` it is a literal excerpt of the source (see below). |
| `mechanism_ids` | list of string | ids of the mechanism map. Until a dedicated map exists these are the topic folder names under `knowledge/` (for example `ctl-retention`). This is a convention, not a verified mapping. |
| `related_claim_ids` | list of string | other claims of the same file (same source, contradicting, or superseding) |

### Labels

| label | meaning |
|---|---|
| `SOURCE_REPORTED` | the source states it (abstract, figure, table, equation) |
| `AUTHOR_INTERPRETATION` | the authors' interpretation or claim; not checked against their data |
| `ENGINEERING_INFERENCE` | an inference made in this project from physics, not stated by the source |
| `UNKNOWN` | the source does not say; recorded so the gap is visible |
| `EXTRAPOLATION_ONLY` | a transfer to another device, geometry, temperature or time scale without support |

### Evidence grades

| grade | meaning |
|---|---|
| A | measured, or reproduced with runnable code |
| B | literature plus a calculation in the same domain |
| C | physically consistent hypothesis |
| D | unverified suggestion |

Convention used for the W40 ledger (an assumption, flagged for review): a claim that only restates abstract text and
whose body is unchecked is graded `C`, the same convention the W40 draft report uses.

## Hard rules (checked by `claims-validate`)

1. `SOURCE_REPORTED` with `access: abstract_only` may only restate abstract content, so `location.kind` must be `abstract`.
2. An `abstract_only` claim with `claim_type: mechanism` cannot be grade `A` or `B`.
3. `label`, `grade`, `access`, `status`, `claim_type` must be in the vocabularies above; `id` unique; `related_claim_ids` must exist.
4. A claim's `access` must equal the access declared for its DOI in `sources[]`.

## Rules not checked by a program (author and reviewer duties)

- The `text` of a `SOURCE_REPORTED` claim must be a literal excerpt of the source. The W40 file was built that way and the
  excerpts were verified against the stored Crossref abstract records at build time; the linter does not re-check this because
  those records are not stored on `main`.
- Never invent a DOI, number, figure or condition. Use `UNKNOWN`.
- 3D VNAND claims keep the cylindrical, coaxial channel hole as the default. A source result for another geometry carries that geometry in `conditions.geometry`.
- Numbers in a ledger are case conditions of a source, not general product values. Do not enter in-house confidential values.
