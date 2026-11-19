# Validation Baseline

This document records the validation baseline for the Phase 1 content and
SEO/AEO repairs, the WP6 Open Graph unification, the WP7 hreflang and
internationalization repair, the before/after numbers, and the debt that
remains intentionally unfixed.

- Date: 2026-11-12
- Source commit (`HEAD`): `b55e39181fbf0ff336147f551804f7357c9a54ae`
- Hugo: `0.147.0` Extended, `windows/amd64`
- The current SEO/AEO baseline was regenerated from the working tree at the
  Phase 1 commit (`HEAD`) with the uncommitted WP6 and WP7 changes. Its
  `source_commit` field therefore names the Phase 1 commit, not a commit that
  contains WP6 or WP7.

## Method

Both validators use a finding-based baseline:

- A finding is identified by `(path, rule, detail)`.
- Each entry stores an occurrence count and the affected line numbers.
- A new occurrence of a known finding fails validation.
- Removing an occurrence leaves a stale baseline entry until the baseline is
  pruned with `--update-baseline`.
- A baseline never exempts a whole file.

This prevents a known issue in one location from silently permitting the same
issue elsewhere in the same file.

## Reproduce

```bash
# 1. Production-equivalent build
HUGO_ENVIRONMENT=production TZ=Europe/Berlin \
  hugo --gc --minify \
  --baseURL "https://agent-engine-optimization.com/" \
  --destination public --cleanDestinationDir

# 2. Content checks (Markdown and front matter)
python -X utf8 scripts/validate_content.py

# 3. Rendered-site checks (reads public/)
python -X utf8 scripts/validate_seo.py
```

Both validators must exit with `0` and print `baseline is current`.

## Pre-change snapshot

At commit `6e4de63`, before the approved Phase 1 edits:

| Validator | Occurrences | Unique findings | Files with findings |
| --- | ---: | ---: | ---: |
| Content | 6,919 | 4,435 | 825 |
| SEO/AEO | 3,193 | 3,189 | 974 |

SEO/AEO was generated from a clean reference build with 977 HTML files and 6
sitemap files.

## Phase 1 changes

1. **Language links:** 2,014 relative `/es/docs/` Markdown link targets in
   German, Portuguese, and Japanese files were changed to the document's own
   language. This covered 1,934 valid links and 80 malformed `] (/es/docs/...)`
   links in 558 files and 110 distinct target slugs.
   - Every target-language file existed before a replacement was applied.
   - External links, fenced code, inline code, and non-link prose mentions were
     left unchanged.
   - The complete audit report is
     `validation/language-link-dry-run.json`.
2. **Meta descriptions:** 198 `metaDescription` overrides in German,
   Portuguese, and Japanese files were removed because each was an exact copy
   of the Spanish description. Every affected file has a non-empty localized
   `description`, which is now the rendered fallback.
3. **Open Graph image:** `static/images/og-default.png` was added as a valid
   1200x630 RGB PNG (20,233 bytes). It matches the existing SVG design and is
   referenced as `https://agent-engine-optimization.com/images/og-default.png`.

## Before and after

### Content validator

| Rule | Before | After |
| --- | ---: | ---: |
| `link.spanish_in_translation` | 2,014 | 0 |
| `link.broken_space` | 388 | 308 |
| `markdown.heading_after_rule` | 6 | 6 |
| `markdown.heading_no_space` | 328 | 328 |
| `markdown.table_separator` | 2,591 | 2,591 |
| `markdown.table_separator_empty` | 980 | 980 |
| `markdown.table_separator_glued` | 24 | 24 |
| `metadata.meta_description_from_spanish` | 198 | 0 |
| `weight.duplicate` | 390 | 390 |
| **Total occurrences** | **6,919** | **4,627** |
| **Unique findings** | **4,435** | **2,152** |
| **Files with findings** | **825** | **762** |

The link fix alone reduced the total to 4,825 occurrences / 2,350 unique
findings / 801 files. Removing the 198 copied meta descriptions reduced it
further to the current 4,627 / 2,152 / 762.

### SEO/AEO validator

| Rule | Before | After |
| --- | ---: | ---: |
| `aeo.agent_manifest_language_missing` | 4 | 4 |
| `aeo.agent_manifest_relative_url` | 2 | 2 |
| `aeo.agent_manifest_updated_stale` | 1 | 1 |
| `aeo.llms_txt_missing_article` | 87 | 87 |
| `aeo.og_image_asset_missing` | 1 | 0 |
| `seo.description_from_spanish` | 198 | 0 |
| `seo.hreflang_missing` | 1 | 1 |
| `seo.hreflang_x_default_missing` | 970 | 970 |
| `seo.og_image_missing` | 1 | 1 |
| `seo.schema_inlanguage_missing` | 960 | 960 |
| `seo.schema_inlanguage_wrong` | 8 | 8 |
| `seo.schema_publisher_unresolved` | 960 | 960 |
| **Total occurrences** | **3,193** | **2,994** |
| **Unique findings** | **3,189** | **2,990** |
| **Files with findings** | **974** | **973** |

The 199 fixed SEO/AEO findings are the 198 Spanish descriptions plus the
missing OG asset. The new PNG is valid, 1200x630, and the rendered
`og:image` URL is absolute and present in `public/`.

## WP6 changes: Open Graph metadata

WP6 unified the rendered Open Graph image across all relevant pages.

1. `layouts/index.html` now references
   `https://agent-engine-optimization.com/images/og-default.png` instead of
   `og-default.svg` for all five language home pages (`/`, `/de/`, `/es/`,
   `/ja/`, `/pt/`).
2. `static/tools/aeo-readiness-checker.html` now renders exactly one absolute
   `og:image` tag pointing at the same PNG. Its checker logic, scripts, and
   external dependencies are unchanged.
3. `scripts/validate_seo.py` now additionally rejects multiple `og:image` tags
   (`seo.og_image_multiple`) and a non-default image on any of the five home
   pages (`seo.og_image_home_not_default`). Existing checks for missing,
   relative, and absent local assets remain in place.

### WP6 before and after

| Metric | Before WP6 | After WP6 |
| --- | ---: | ---: |
| Non-alias HTML pages (incl. five 404 pages) | 976 | 976 |
| Pages with an Open Graph image | 975 | 976 |
| Home pages with the PNG | 0 of 5 | 5 of 5 |
| Tools page with an Open Graph image | 0 of 1 | 1 of 1 |
| `seo.og_image_missing` findings | 1 | 0 |

The SEO/AEO baseline lost exactly one entry:
`public/tools/aeo-readiness-checker.html` / `seo.og_image_missing`. No other
baseline entry was added, removed, or changed. Totals moved from 2,994
occurrences / 2,990 unique findings to 2,993 / 2,989; files with findings
remained 973 because the tools page still carried its hreflang finding at that
point. WP7 later fixed that finding.

The build contains 977 HTML files: 976 non-alias pages (971 content pages plus
the five language 404 pages) and one alias (`en/index.html`). The validator
checks the 971 content pages and by design skips `404.html`; a separate QA
check covered all 976 non-alias pages for the WP6 image requirements.

## WP7 changes: hreflang and internationalization

WP7 unified the language signals for the five configured languages.

1. `layouts/partials/hreflang.html` is the single source of hreflang output.
   It renders one self-referencing link per entry in `.AllTranslations`, using
   `.Language.LanguageCode`, and then one `x-default` link. It emits nothing on
   pages whose `.Kind` is `404`.
2. `layouts/partials/docs/html-head.html`, `layouts/index.html`, and
   `static/tools/aeo-readiness-checker.html` consume that logic or declare
   their self-referencing links directly. The tools page is a static file and
   is not part of the Hugo translation graph.
3. `layouts/baseof.html` and `layouts/index.html` render `html lang` from
   `.Language.LanguageCode`. Portuguese therefore outputs `pt-BR` while the URL
   prefix remains `/pt/`. `config.toml` is unchanged.
4. `scripts/validate_seo.py` derives the allowed codes from the `[languages.*]`
   blocks in `config.toml`, fixes `normalize_language("x-default")`, and adds
   nine new HTML hreflang rules and five new sitemap hreflang rules listed
   below. The pre-existing `seo.hreflang_incomplete` rule remains active.

### Language codes and x-default strategy

| Language | HTML `hreflang` / `html lang` | URL prefix |
| --- | --- | --- |
| English | `en` | `/` |
| Spanish | `es` | `/es/` |
| German | `de` | `/de/` |
| Portuguese | `pt-BR` | `/pt/` |
| Japanese | `ja` | `/ja/` |

`x-default` points to the English equivalent of the same route. All five home
pages point to `/`. A localized documentation page points to the English
article with the same slug. The tools page points to itself. When no English
equivalent exists, the partial falls back to `/`; the validator records
`seo.hreflang_unexpected` or `seo.hreflang_x_default_wrong` as appropriate.
No hreflang or x-default link points to the `/en/` redirect alias. The five
404 pages emit no hreflang and no x-default.

Hugo's built-in sitemap templates and configuration were not changed. The
sitemap keeps its five child sitemaps with 194 URLs each (970 total), absolute
and reciprocal alternates, and no x-default or tools page entry.

### Validator rules added in WP7

WP7 added nine HTML hreflang rules:
`seo.hreflang_invalid_code`, `seo.hreflang_not_absolute`,
`seo.hreflang_target_missing`, `seo.hreflang_self_mismatch`,
`seo.hreflang_not_reciprocal`, `seo.hreflang_target_alias`,
`seo.hreflang_unexpected`, `seo.hreflang_x_default_wrong`, and
`seo.hreflang_sitemap_mismatch`.

WP7 added five sitemap hreflang rules:
`aeo.sitemap_hreflang_target_missing`,
`aeo.sitemap_hreflang_not_absolute`, `aeo.sitemap_hreflang_duplicate`,
`aeo.sitemap_hreflang_self_missing`, and
`aeo.sitemap_hreflang_not_reciprocal`.

These hreflang rules already existed and remain active; they were not added
in WP7: `seo.hreflang_missing`, `seo.hreflang_incomplete`,
`seo.hreflang_self_missing`, `seo.hreflang_x_default_missing`, and
`seo.hreflang_duplicate`.

WP6 introduced two Open Graph rules separately from the WP7 hreflang work:
`seo.og_image_multiple` and `seo.og_image_home_not_default`.

All pre-existing canonical, title, description, Open Graph, JSON-LD, sitemap
target, and AEO checks remain active. No global exemptions, directory
allowlists, or language allowlists were introduced.

### WP7 before and after

| Metric | Before WP7 | After WP7 |
| --- | ---: | ---: |
| SEO/AEO occurrences | 2,993 | 2,022 |
| Unique findings | 2,989 | 2,018 |
| Files with findings | 973 | 966 |
| `seo.hreflang_x_default_missing` | 970 | 0 |
| `seo.hreflang_missing` | 1 | 0 |

The prune removed exactly 971 finding groups: 970
`seo.hreflang_x_default_missing` and one `seo.hreflang_missing` on
`public/tools/aeo-readiness-checker.html`. No other baseline entry was added,
removed, or changed. `validation/content-baseline.json` is unchanged
(SHA-256 `81C726CEC2E1CEDDBE12C3A7CEC022831F41A54D840418BDF7457A5D5554ADDD`).
The SEO/AEO baseline after pruning has SHA-256
`0AA36D772C1E09C523A0731040B2CABB00C390DE11DE559894843335B2F0C1F6`.

## WP7-R1 corrections

The independent audit of 2026-11-12 found gaps in the WP7 validator logic.
WP7-R1 hardened `scripts/validate_seo.py` without changing rendered output,
templates, content, or either baseline.

1. Language codes are compared exactly. `pt-BR` is correct for Portuguese and
   `pt` is rejected. The same exact comparison is used for `html lang`,
   HTML/sitemap hreflang codes, and schema `inLanguage`.
2. A sitemap self-reference must match both the entry route and the configured
   language code. An x-default-only self-reference, a wrong code, a mixed
   correct/wrong code, and a missing self-reference are findings. Codes outside
   the configured set are additionally reported as
   `aeo.sitemap_hreflang_invalid_code`.
3. Duplicate sitemap `<loc>` entries are reported as
   `aeo.sitemap_duplicate_loc`; all occurrences still pass through the other
   sitemap checks.
4. Malformed URLs are converted into controlled findings instead of aborting
   with `ValueError`. This covers `urlsplit`, route resolution, hreflang
   targets, canonical and Open Graph URLs, and sitemap parsing. `http://[::1`
   and URLs with invalid ports are covered by synthetic tests.
5. All five rendered 404 pages are validated explicitly for absent
   hreflang/x-default links, an existing canonical, and a valid 1200x630 Open
   Graph image. They are not treated as indexable documentation pages.
6. The root sitemap must be a valid `<sitemapindex>` with `<sitemap>` entries
   and non-empty `<loc>` targets. A valid `<urlset>` root is reported as
   unexpected, and an invalid root is reported instead of yielding an empty
   result.
7. Nested documentation routes such as `/docs/foo/bar/` and
   `/de/docs/foo/bar/` are grouped by their full slug. x-default points to the
   English page with the same nested slug. Flat routes keep their previous
   behavior.

R1-only rule names introduced by these checks are:
`seo.canonical_invalid`, `seo.og_image_invalid`, `seo.og_image_dimensions`,
`seo.hreflang_url_invalid`, `seo.hreflang_on_404`,
`seo.hreflang_on_404_target_invalid`, `aeo.sitemap_root_invalid`,
`aeo.sitemap_root_unexpected`, `aeo.sitemap_index_empty`,
`aeo.sitemap_index_loc_missing`, `aeo.sitemap_child_invalid_url`,
`aeo.sitemap_child_root_invalid`, `aeo.sitemap_url_loc_missing`,
`aeo.sitemap_url_invalid`, `aeo.sitemap_duplicate_loc`,
`aeo.sitemap_hreflang_url_invalid`, and
`aeo.sitemap_hreflang_invalid_code`.

The existing baselines were not regenerated or edited. They remain at 2,022
SEO/AEO occurrences / 2,018 unique findings / 966 files and 4,627 content
occurrences / 2,152 unique findings / 762 files. The stricter rules produce no
new findings on the current production build.

R1 verification on the production build:

```text
Hugo build:        exit 0, 977 HTML files, 6 sitemap files, PT warning unchanged
Content validator: exit 0, 4,627 occurrences, 2,152 unique, 762 files
SEO/AEO validator: exit 0, 2,022 occurrences, 2,018 unique, 966 files
New/fixed:         0 / 0 for both validators
Independent QA:    5 homepages, 965 docs pages, 1 tools page, 5 404 pages,
                   970 sitemap URLs in 5 child sitemaps, 976/976 pages with
                   one absolute 1200x630 Open Graph image, 0 duplicates
Synthetic tests:   26/26 passed
```

## Remaining known debt

These findings are recorded in the current baselines and were deliberately
left unfixed.

### Content

| Rule | Occurrences | Why it remains |
| --- | ---: | --- |
| `link.broken_space` | 308 | Outside the approved Spanish-link scope; these are other malformed link targets. |
| `markdown.table_separator` | 2,591 | Mass table repair was explicitly excluded. Most are `---|` separators. |
| `markdown.table_separator_empty` | 980 | Lone-pipe separator rows; same excluded table repair. |
| `markdown.table_separator_glued` | 24 | Separator and first data row are glued together. |
| `markdown.heading_no_space` | 328 | Heading markers without a space after `#`. |
| `markdown.heading_after_rule` | 6 | Headings glued to a horizontal rule. |
| `weight.duplicate` | 390 | Pre-existing duplicate weights within languages. |

### SEO/AEO

| Rule | Occurrences | Why it remains |
| --- | ---: | --- |
| `seo.schema_inlanguage_missing` | 960 | Article JSON-LD lacks `inLanguage`; a schema/template change was not approved. |
| `seo.schema_publisher_unresolved` | 960 | Publisher `@id` is referenced but not defined in the page graph. |
| `aeo.llms_txt_missing_article` | 87 | English articles are not listed in `static/llms.txt`. |
| `aeo.agent_manifest_language_missing` | 4 | The manifest lists only `en`, not `es`, `pt`, `de`, `ja`. |
| `aeo.agent_manifest_relative_url` | 2 | Manifest capability URLs use relative paths. |
| `aeo.agent_manifest_updated_stale` | 1 | Manifest `updated` date predates the newest content. |
| `seo.schema_inlanguage_wrong` | 8 | Four language homepages contain two schema nodes with `inLanguage: en`. |

The SEO/AEO validator now reports 966 files with findings, down from 973 after
WP6. Seven files therefore became completely finding-free. The 971 removed
finding groups are not 971 finding-free files: most files that lost the
x-default finding still carry other baseline findings such as
`seo.schema_inlanguage_missing` or `seo.schema_publisher_unresolved`.

## Verification result

Final Phase 1 run:

```text
Hugo build:        exit 0, 977 HTML files, 6 sitemap files, OG PNG present
Content validator: exit 0, 4,627 occurrences, 2,152 unique, 762 files
SEO/AEO validator: exit 0, 2,994 occurrences, 2,990 unique, 973 files
New findings:      0 for both validators
```

Final WP6 run:

```text
Hugo build:        exit 0, 977 HTML files, 6 sitemap files, PT warning unchanged
Content validator: exit 0, 4,627 occurrences, 2,152 unique, 762 files
SEO/AEO validator: exit 0, 2,993 occurrences, 2,989 unique, 973 files
New findings:      0 for both validators
Open Graph QA:     976/976 non-alias pages with an image, 5/5 home pages with the
                   PNG, 0 duplicate tags, 0 relative URLs, 0 missing local assets
```

Final WP7 run:

```text
Hugo build:        exit 0, 977 HTML files, 6 sitemap files, PT warning unchanged
Content validator: exit 0, 4,627 occurrences, 2,152 unique, 762 files
SEO/AEO validator: exit 0, 2,022 occurrences, 2,018 unique, 966 files
New findings:      0 for both validators
Hreflang QA:       971/971 pages with correct self-reference and x-default,
                   971/971 reciprocal, 5/5 404 pages hreflang-free,
                   970/970 sitemap entries self-referencing and reciprocal,
                   970/970 HTML/sitemap language sets and URLs consistent
Synthetic tests:   18/18 error types detected, correct page and sitemap clean
```

Both baselines were pruned with `--update-baseline` only after the new-finding
count was zero. `--force` was not used. The WP6 prune removed only the
tools-page `seo.og_image_missing` entry. The WP7 prune removed only the 970
`seo.hreflang_x_default_missing` entries and the one `seo.hreflang_missing`
entry; no other entry was added, removed, or changed.

## Baseline update policy

- Run both validators after every content or template change.
- Fix new findings; do not add them to the baseline.
- When intentional fixes remove findings, run `--update-baseline` for the
  affected validator.
- Review the diff of the baseline JSON before accepting it.
- Never use `--force` without explicit review, and never regenerate a baseline
  solely to obtain a green check.

## Limitations

- The SEO/AEO validator reads `public/` and therefore requires a build. It does
  not validate the Markdown sources directly.
- Meta-description length is not enforced. Fifty-two localized descriptions
  exceed 160 characters; 14 of them are among the 198 files whose copied
  Spanish `metaDescription` was removed. This is pre-existing content.
- The baseline `files` field counts files with at least one finding, not all
  files in the repository.
- The baseline `source_commit` field records `HEAD`. For the current baseline
  that is the Phase 1 commit, which does not contain the uncommitted WP6 or WP7
  changes. The `generated_at` timestamps and this document describe the actual
  working-tree state.
- The theme's `layouts/404.html` hardcodes `.Site.Language.Lang`, so the
  Portuguese 404 page still renders `html lang="pt"`. The 404 pages are
  noindex and outside the sitemap, and WP7 was scoped to hreflang suppression
  there; changing the theme file was outside the approved file scope.
