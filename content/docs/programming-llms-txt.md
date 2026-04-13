---
title: "How to Write llms.txt Correctly So AI Agents Find Your Website Instantly"
date: 2026-04-12
weight: 62
category: "Guide"
description: "llms.txt is the simplest and most powerful agent discovery mechanism. Exact structure, content rules, dynamic generation for large sites, and integration with schema markup."
summary: "llms.txt tells AI agents what your site offers and how to interact with it. This guide covers the exact format, content rules, common mistakes, and how to generate it dynamically for large sites."
keywords:
  - llms.txt guide
  - llms.txt format
  - how to write llms.txt
  - agent discovery llms.txt
  - llms.txt implementation
---

llms.txt is the simplest and most effective way to make AI agents discover your website. One Markdown file in your site root tells agents what you offer, where to find it, and how to interact with it. Agents check for llms.txt before crawling the full site, so getting it right means getting discovered first.

## Why llms.txt is non-negotiable in 2026

AI agents follow a discovery hierarchy when encountering a new site. First, check for llms.txt. Second, check for agent-card.json. Third, look for structured data in the HTML. Fourth, attempt to parse the raw page content.

A site without llms.txt forces agents to start at step three or four, which is slower, less reliable, and more likely to produce inaccurate extraction. A site with a clear llms.txt lets agents understand the full scope of your offering in a single request.

Stripe, Cloudflare, and Cursor already publish llms.txt files. Sites that adopted early report significantly higher agent interaction rates and more accurate citations in AI-generated answers.

## The exact structure

llms.txt is a Markdown file. It uses headings to organize information and plain text for descriptions. Here is the recommended structure:

**Line 1: Site name as H1 heading.** One line, plain text.

**Section 1: What this site offers.** A brief paragraph (2 to 3 sentences) describing your product, service, or content in factual terms. No marketing language. State what you do, who it is for, and what makes it useful.

**Section 2: Key pages.** A list of your most important URLs with a one-line description of each. Include your homepage, core product or service pages, pricing page, documentation, and any pages where agents should look for specific information.

**Section 3: Available endpoints.** If your site exposes API endpoints or MCP tools, list them with brief descriptions of what each one does, what inputs it requires, and what it returns.

**Section 4: Authentication.** State how agents should authenticate, or explicitly state that no authentication is required for read access.

**Section 5: Constraints.** Rate limits, usage policies, data freshness guarantees, and any restrictions on how agents should interact with your site.

**Section 6: Contact.** How to report errors or request clarification.

## Content rules

Write for extraction, not persuasion. Every sentence should contain a fact that an agent can use. Remove adjectives that do not carry information. Replace "our powerful platform" with "API-based scheduling platform for healthcare providers."

Keep descriptions to one or two sentences per item. Agents do not need paragraphs. They need precise claims they can match against user queries.

Update llms.txt whenever you add, remove, or change a significant capability. An outdated llms.txt that describes features you no longer offer is worse than no llms.txt at all because it causes agents to attempt actions that will fail.

## Dynamic generation for large sites

Sites with hundreds of products or frequently changing inventory should generate llms.txt dynamically rather than maintaining it manually.

Build a script that queries your product database, extracts the current catalog summary, lists active API endpoints from your route configuration, and writes the output as a Markdown file. Run this script on a schedule (daily for most sites, hourly for inventory-heavy sites).

For Hugo-based sites, you can generate llms.txt as part of the build process by creating a custom output format that renders your content data as Markdown.

## Integrating llms.txt with schema markup

llms.txt and schema markup serve complementary purposes. llms.txt provides site-level discovery (what does this entire site offer). Schema markup provides page-level detail (what does this specific page contain).

Reference your llms.txt from your schema markup by including it in your WebSite schema as a potentialAction target. Reference your most important schema-marked pages from your llms.txt key pages section.

This creates a two-layer discovery system: agents that start with llms.txt find the schema-marked pages faster, and agents that start with a specific page can navigate to llms.txt for the full site picture.

## Comparison: with vs without llms.txt

| Metric | Without llms.txt | With llms.txt |
|---|---|---|
| Agent discovery rate | Below 10 percent | Up to 80 percent |
| Time to first agent interaction | Days (requires crawling) | Seconds (single file read) |
| Extraction accuracy | Variable (depends on page quality) | High (structured overview) |
| Agent return rate | Low | Significantly higher |

## Common mistakes

Writing llms.txt as marketing copy. Agents do not respond to persuasion. They respond to structured facts. Every line should answer a specific question about what your site can do.

Listing every page on the site. llms.txt is not a sitemap. Include only the pages that matter most for agent interaction. For a 500-page site, the llms.txt should reference 10 to 30 key pages.

Forgetting to update it. An llms.txt that references deprecated endpoints or discontinued products actively harms agent trust.

The [AEO implementation guide](/docs/implement-aeo/) covers how llms.txt fits into the broader optimization path.

---

## FAQ

**Where exactly should llms.txt be placed?**
At the root of your domain: yourdomain.com/llms.txt. Agents look for it at this exact path, similar to robots.txt.

**What format should llms.txt use?**
Markdown. Use headings for sections and plain text for descriptions. No HTML, no JSON, no custom formats.

**How long should llms.txt be?**
One to two pages of concise text. Long enough to cover your key offerings and endpoints. Short enough that an agent can process it in a single read.

**Should llms.txt include pricing information?**
Yes, if your pricing is public. Include base pricing, pricing model (per seat, per usage, flat rate), and where to find detailed pricing information.

**Can I have different llms.txt for different subdomains?**
Yes. Each subdomain should have its own llms.txt that describes that subdomain's specific capabilities.
