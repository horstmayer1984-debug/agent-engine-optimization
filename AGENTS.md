# Repository Rules for AI Agents

This repository builds the multilingual Hugo site
`agent-engine-optimization.com`. These rules apply to every change, including
content, layouts, configuration, scripts, and validation data.

## Language policy

- English is the sole canonical content source. English files are
  `content/docs/<slug>.md`.
- Spanish, German, Portuguese, and Japanese are equal target languages:
  `content/docs/<slug>.es.md`, `.pt.md`, `.de.md`, and `.ja.md`.
- Translate from English only. Never use one translation as the source for
  another translation.
- Every translation must carry localized front matter, especially `title`,
  `description`, `summary`, and `keywords`.
- Do not copy a Spanish `metaDescription` or `description` into another
  language. If no localized `metaDescription` exists, the localized
  `description` is the intended fallback.
- Internal links in a translation must point to the same language:
  `/de/docs/...` in German, `/pt/docs/...` in Portuguese, `/ja/docs/...` in
  Japanese. Do not send readers of one translation to `/es/docs/` merely
  because the Spanish page exists.
- External links and deliberately cited Spanish sources must not be rewritten
  by bulk language-link repairs.

## Content layout and front matter

- One slug has one file per language. The language suffix is part of the file
  name, not the URL slug.
- Do not rename files, slugs, or routes without explicit approval. A rename
  changes public URLs and requires a redirect decision.
- Required front matter: `title`, `description`, `date`, `weight`, `category`.
- Optional but supported: `metaTitle`, `metaDescription`, `summary`,
  `keywords`.
- The rendered description precedence is:
  `metaDescription` -> localized `description` -> `.Description` ->
  `summary` -> `.Summary` -> site description.
- Dates use `YYYY-MM-DD`; weights are integers and must be unique within a
  language.
- Use UTF-8 without a BOM. Preserve the file's existing line endings and avoid
  whole-file rewrites that create noisy diffs.

## Build environment

- Hugo Extended **0.147.0** is the pinned version used by CI.
- The theme is the `themes/hugo-book` Git submodule. Initialize it with:
  `git submodule update --init --recursive`.
- Production-equivalent local build:

  ```bash
  HUGO_ENVIRONMENT=production TZ=Europe/Berlin \
    hugo --gc --minify \
    --baseURL "https://agent-engine-optimization.com/" \
    --destination public --cleanDestinationDir
  ```

  On PowerShell, set `$env:HUGO_ENVIRONMENT` and `$env:TZ` first.
- The known Hugo warning
  `Failed to get translated string for language "pt" and ID "bookSearchConfig"`
  is pre-existing and does not fail the build.

## Validation is mandatory

Both validators must pass with **0 new findings** and a **current baseline**:

```bash
python -X utf8 scripts/validate_content.py
python -X utf8 scripts/validate_seo.py
```

- `validate_content.py` checks Markdown, front matter, language files, links,
  table separators, headings, duplicate weights, and copied Spanish metadata.
- `validate_seo.py` checks the generated `public/` site: titles, descriptions,
  canonicals, hreflang, JSON-LD, Open Graph assets, sitemaps, `llms.txt`, and
  the agent manifest.
- Build before running the SEO/AEO validator. It reads `public/`, not the
  Markdown sources.
- Exit code `0` means no new findings and no fixed baseline entries.
  Exit code `1` means new findings or a stale baseline. Exit code `2` means a
  configuration or baseline-format error.

### Baseline rules

- `validation/content-baseline.json` and `validation/seo-baseline.json` record
  known debt by `(path, rule, detail)` and occurrence count. They are not
  file-level exemptions.
- A new occurrence of a known issue fails validation.
- When findings are intentionally fixed, prune the baseline with
  `--update-baseline` only after confirming that there are no new findings.
- Never use `--force` to bless new findings without explicit review.
- Never delete, empty, or regenerate a baseline just to make a check pass.
- See `VALIDATION_BASELINE.md` for the current numbers and known debt.

## Scope and safety

- Do not modify or delete `AUDIT_GOLDANKAUF_ENZ/`; it is pre-existing local
  audit material.
- Keep changes small and reviewable. Do not mix content fixes with unrelated
  table, heading, navigation, template, or deployment changes.
- Do not change the GitHub Actions workflow, Pages configuration, or
  deployment behavior as part of a content fix.
- Do not commit, push, or deploy without explicit instruction. A push to
  `main` triggers the GitHub Pages deployment workflow.
- After each work package, report the files changed, the changes made, the
  validation commands run, and their results.
- Stop and ask before proceeding if a change has unexpected side effects or
  requires work outside the approved scope.

## SEO and AEO requirements

- Every rendered page needs one title, one non-empty meta description, a
  self-referencing canonical URL, and a correct `html lang`.
- Hreflang must include the page's own language and the other configured
  languages for which the page exists. `x-default` is required by the
  validator but is still known debt on most pages; do not add new pages
  without it.
- The default Open Graph image is
  `static/images/og-default.png`, exactly 1200x630 PNG, referenced through
  `params.images` as an absolute site URL.
- JSON-LD must be valid JSON. Article nodes need `inLanguage`; publisher
  `@id` references must resolve within the page graph.
- Keep `static/llms.txt` and `static/.well-known/agent-manifest.json` in sync
  when adding or renaming English content. The manifest currently lists only
  `en`, uses relative capability URLs, and has a stale `updated` date; these
  are tracked baseline findings, not patterns to copy.

## Autonomous model selection and orchestration

Execute at every prompt:
- Autonomously plan and break down the request into concrete execution phases without asking for unnecessary micro-approvals.
- Select the optimal AI model for the task and for any subagents/delegates according to `.agents/skills/autonomous-model-orchestrator/SKILL.md` (Tier 1 Fast/Routine, Tier 2 Balanced/Standard, Tier 3 Frontier/Reasoning).
- Orchestrate subagents, parallelize independent operations, batch tool calls efficiently, and verify all outcomes deterministically before completing.

