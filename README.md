# CIVITAS ATLAS

Independent research project on network communities, startup societies and emerging forms of governance, maintained by **Azamat Safarov**.

**Website:** https://polis-network-atlas.vercel.app  
**Contact / corrections / rights:** akutagavasora777@gmail.com

## Scope

The live research snapshot contains 152 merged project records. It is not a census of all network states or a list of recognized sovereign states. Claims, chronology and statistics remain attributable to sources and are not all independently verified.

## Open participation, not a blanket open-data claim

This repository opens our original frontend code, contribution rules and an index of source URLs. It does **not** grant rights to upstream databases, descriptions, photos, logos or social posts. Those materials are excluded from this repository while redistribution permissions remain unresolved. Public access to the website is not a data license.

New original community submissions are stored in `data/community-submissions.json`. Contributors agree to publish their original submission under CC BY 4.0, with their attribution. Do not submit material you do not have permission to license. MIT applies only to our original code.

## Add a project

[Open a project submission](https://github.com/AzamatSafarov/civitas-atlas/issues/new?template=project.yml) or fork the repository and edit `data/community-submissions.json`, then open a pull request. Submission does not guarantee inclusion; changes require editorial review. The repository is **not yet connected to automatic production deployment**.

Requirements: official source, clear location or explicit virtual status, source-linked factual claims, author attribution and rights to submitted text/media. Do not include private personal data, secrets or identity documents. No advertising ranking or pay-for-inclusion scheme.

## Development

The frontend files preserve the current implementation. The full runtime corpus, image cache and third-party vendor assets are intentionally excluded; do not expect the live globe to run from this checkout alone. `python preview.py` runs a self-contained contribution portal at http://127.0.0.1:8850. This portal is separate from the full atlas.

Validate submissions: `python scripts/validate_submissions.py`. GitHub CI validates JSON submissions; no production deployment is triggered.

## Research method

Maintain source-specific records instead of overwriting conflicts. Distinguish planned, historical, active and virtual nodes. Never invent coordinates. "Network state" is a project/category label, not recognition. An editor may decline, relabel or remove a record with reasons; disputes can be raised as issues or by email.

## Licenses and policy

See [RIGHTS.md](RIGHTS.md), [PRIVACY.md](PRIVACY.md), [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Legal text is operational guidance, not a legal opinion or immunity from claims.
