# Agent Engine Optimization

Source repository for [agent-engine-optimization.com](https://agent-engine-optimization.com/),
a multilingual Hugo site about Agent Engine Optimization (AEO): the read layer
that makes content discoverable and the execution layer that lets autonomous
agents act on it.

## Stack

- Hugo Extended **0.147.0** (the version pinned in CI)
- Hugo Book theme, included as the `themes/hugo-book` Git submodule
- GitHub Pages deployment through `.github/workflows/deploy.yml`
- Python 3.10+ for the repository validators (standard library only)

## Languages

| Language | Code | Content suffix | Route |
| --- | --- | --- | --- |
| English (canonical) | `en` | none | `/docs/<slug>/` |
| Spanish | `es` | `.es.md` | `/es/docs/<slug>/` |
| Portuguese | `pt` | `.pt.md` | `/pt/docs/<slug>/` |
| German | `de` | `.de.md` | `/de/docs/<slug>/` |
| Japanese | `ja` | `.ja.md` | `/ja/docs/<slug>/` |

English is the only source language. Spanish, German, Portuguese, and Japanese
are translated from English and are equal target languages. Do not translate
from one translation into another.

## Quick start

```bash
git clone --recurse-submodules <repository-url>
cd agent-engine-optimization
hugo server
```

If the repository was cloned without submodules:

```bash
git submodule update --init --recursive
```

`hugo server` serves the site locally, usually at
`http://localhost:1313/`. Hugo Extended 0.147.0 must be installed and available
on `PATH`.

## Production build

Bash:

```bash
HUGO_ENVIRONMENT=production TZ=Europe/Berlin \
  hugo --gc --minify \
  --baseURL "https://agent-engine-optimization.com/" \
  --destination public --cleanDestinationDir
```

PowerShell:

```powershell
$env:HUGO_ENVIRONMENT = "production"
$env:TZ = "Europe/Berlin"
hugo --gc --minify `
  --baseURL "https://agent-engine-optimization.com/" `
  --destination public --cleanDestinationDir
```

The build writes to `public/`, which is ignored by Git. A current build
produces 977 HTML files and 6 sitemap files. The following warning is
pre-existing and does not fail the build:

```text
Failed to get translated string for language "pt" and ID "bookSearchConfig"
```

## Validation

Build first, then run both validators:

```bash
python -X utf8 scripts/validate_content.py
python -X utf8 scripts/validate_seo.py
```

- `scripts/validate_content.py` checks Markdown and front matter in
  `content/docs/`: language-file completeness, localized metadata, internal
  links, malformed table separators, heading syntax, duplicate weights, and
  encoding.
- `scripts/validate_seo.py` checks the rendered `public/` site: titles, meta
  descriptions, canonicals, hreflang, JSON-LD, Open Graph images, sitemaps,
  `llms.txt`, and the agent manifest.

Both commands exit with `0` only when there are no new findings and no fixed
entries left in the baseline. Exit code `1` means new findings or a stale
baseline; exit code `2` means a configuration or baseline-format error.

### Baseline workflow

Known debt is recorded in:

- `validation/content-baseline.json`
- `validation/seo-baseline.json`

Baselines are keyed by file, rule, and finding detail, including an occurrence
count. They do not exempt whole files. Adding a new occurrence of a known issue
fails validation.

After intentionally fixing findings and confirming that there are **no new
findings**, prune the baseline:

```bash
python -X utf8 scripts/validate_content.py --update-baseline
python -X utf8 scripts/validate_seo.py --update-baseline
```

`--update-baseline` refuses to write when new findings are present. Do not use
`--force` to bypass that protection without explicit review. See
`VALIDATION_BASELINE.md` for the current counts and the remaining known debt.

## Deployment

`.github/workflows/deploy.yml` builds the site with Hugo Extended 0.147.0 and
deploys `public/` to GitHub Pages. It runs on:

- a push to `main`
- manual `workflow_dispatch`

There is no separate local deploy step. Do not push to `main` unless
publication has been explicitly approved.

## Project layout

```text
content/docs/              English and translated Markdown content
layouts/                   Site overrides for the Hugo Book theme
static/                    Images, llms.txt, robots.txt, agent manifest
scripts/                   Content and SEO/AEO validators
validation/                Finding-based baselines and audit reports
themes/hugo-book/          Pinned theme submodule
.github/workflows/         GitHub Pages build and deploy workflow
config.toml                Languages, params, markup, sitemap
```

## Content conventions

- English file: `content/docs/<slug>.md`
- Translation: `content/docs/<slug>.<lang>.md`
- Start with the English file, then translate into all four target languages.
- Required front matter: `title`, `description`, `date`, `weight`, `category`.
- Optional SEO fields: `metaTitle`, `metaDescription`, `summary`, `keywords`.
- If `metaDescription` is absent, the localized `description` is rendered.
- Keep internal links inside the same language, for example
  `/de/docs/execution-layer/` in a German file.
- Do not rename an existing slug or route without an explicit redirect and
  publication decision.
- Use UTF-8 without a BOM and avoid whole-file rewrites.

## Known limitations

- The Portuguese `bookSearchConfig` warning comes from the theme and is
  tracked separately from content validation.
- The baseline still contains the known table, heading, duplicate-weight,
  hreflang, JSON-LD, `llms.txt`, and agent-manifest debt listed in
  `VALIDATION_BASELINE.md`. The baseline is not permission to add more.
- Meta-description length is not currently enforced. Fifty-two localized
  descriptions are longer than 160 characters; 14 of them are among the 198
  files whose copied Spanish `metaDescription` was removed. This is
  pre-existing content, not a Phase 1 regression.
- `AUDIT_GOLDANKAUF_ENZ/` is local audit material and is not part of the site.

Repository rules for automated agents are in `AGENTS.md`.
