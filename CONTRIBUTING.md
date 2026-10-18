# Contributing to CIVITAS ATLAS

Help improve the source-linked record of communities and governance initiatives. Every submission receives editorial review; publication is manual.

## Suggest a project

Use the [project submission form](https://github.com/AzamatSafarov/civitas-atlas/issues/new?template=project.yml). Include:

- The project's name and official website.
- Your own short description and its physical, virtual, planned or historical location.
- Source URLs supporting the claims.
- Permission and attribution for anything you submit.

Do not copy marketing pages, guess coordinates or supply unsupported population, revenue, dates or legal status. A source statement is not automatically a confirmed fact.

## Submit a pull request

Add an original record to `data/community-submissions.json`. Required fields:

| Field | Requirement |
|---|---|
| `id` | Unique lowercase slug, using letters, digits and hyphens |
| `name` | Project name |
| `description` | Your own factual description |
| `location` | Published location or explicit virtual/unknown status |
| `officialURL` | Public HTTPS URL |
| `sourceURLs` | Non-empty list of public HTTPS sources |
| `contributor` | Attribution for the original submission |
| `license` | `CC-BY-4.0` for your original contribution |

Run:

```bash
python scripts/validate_submissions.py
```

Passing validation checks the submission's structure, not factual accuracy or editorial acceptance. Do not change the legacy research snapshot as part of an original-submission PR.

## Review and publication

1. Check topical relevance and possible duplicates.
2. Review official sources and conflicting claims.
3. Check author attribution, permissions and privacy.
4. Accept, request changes or decline with a reason.
5. Publish approved changes through the separate manual site process.

Acceptance does not establish statehood. Original accepted text is contributed under CC BY 4.0; third-party material needs its own permission and attribution. No pay-for-inclusion or advertising ranking is offered.

## Corrections, privacy and rights

Use [Issues](https://github.com/AzamatSafarov/civitas-atlas/issues/new) for public factual corrections. Public issues are visible to everyone: do not post credentials, identity documents or private personal data.

Send private security concerns and rights requests to **akutagavasora777@gmail.com**. For a rights request, include the affected URL, material and requested action. See [RIGHTS.md](RIGHTS.md) and [SECURITY.md](SECURITY.md).

No harassment, impersonation or promotional spam.
