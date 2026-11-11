# Validation Baseline

This document records the validation baseline for the Phase 1 content and
SEO/AEO repairs, the before/after numbers, and the debt that remains
intentionally unfixed.

- Date: 2026-11-11
- Source commit (`HEAD`): `6e4de630a8900462dd4e5002ff15690a4ce5cfe3`
- Hugo: `0.147.0` Extended, `windows/amd64`
- The baselines were generated from the working tree before any Phase 1 change
  was committed. Their `source_commit` field therefore names `HEAD`, not a
  commit that contains the repairs.

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

## Remaining known debt

These findings are recorded in the current baselines and were deliberately not
changed in Phase 1.

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
| `seo.hreflang_x_default_missing` | 970 | The theme does not emit `x-default`; a template change was not approved. |
| `seo.schema_inlanguage_missing` | 960 | Article JSON-LD lacks `inLanguage`; a schema/template change was not approved. |
| `seo.schema_publisher_unresolved` | 960 | Publisher `@id` is referenced but not defined in the page graph. |
| `aeo.llms_txt_missing_article` | 87 | English articles are not listed in `static/llms.txt`. |
| `aeo.agent_manifest_language_missing` | 4 | The manifest lists only `en`, not `es`, `pt`, `de`, `ja`. |
| `aeo.agent_manifest_relative_url` | 2 | Manifest capability URLs use relative paths. |
| `aeo.agent_manifest_updated_stale` | 1 | Manifest `updated` date predates the newest content. |
| `seo.schema_inlanguage_wrong` | 8 | Four language homepages contain two schema nodes with `inLanguage: en`. |
| `seo.hreflang_missing` | 1 | `/tools/aeo-readiness-checker.html` has no alternate links. |
| `seo.og_image_missing` | 1 | The same tools page has no Open Graph image. |

The SEO/AEO validator now reports 973 files with findings. The difference from
the pre-change 974 is the removed missing-asset finding, not a removed page.

## Verification result

Final Phase 1 run:

```text
Hugo build:        exit 0, 977 HTML files, 6 sitemap files, OG PNG present
Content validator: exit 0, 4,627 occurrences, 2,152 unique, 762 files
SEO/AEO validator: exit 0, 2,994 occurrences, 2,990 unique, 973 files
New findings:      0 for both validators
```

Both baselines were pruned with `--update-baseline` only after the new-finding
count was zero. `--force` was not used.

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
- The baseline `source_commit` field records `HEAD`, which does not contain the
  uncommitted Phase 1 changes. The `generated_at` timestamps and this document
  describe the actual working-tree state.
