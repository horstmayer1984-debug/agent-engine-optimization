---
title: "Cloudflare Search, Agent, and Training Crawlers: What AEO Teams Should Do"
metaTitle: "Cloudflare Search vs Agent vs Training Crawlers"
date: 2026-07-02
weight: 188
category: "Analysis"
description: "Cloudflare now separates AI traffic into Search, Agent, and Training crawlers. Learn what this means for AEO, robots.txt, and crawler access."
summary: "A practical AEO guide to Cloudflare's July 2026 AI traffic taxonomy for Search, Agent, and Training crawlers."
keywords:
  - Cloudflare Search Agent Training crawlers
  - AI crawler taxonomy
  - agent crawler access
  - AI traffic controls
  - AEO crawler policy
---

# Cloudflare Search, Agent, and Training Crawlers

Cloudflare's July 2026 AI traffic controls split automated AI traffic into three practical categories: Search, Agent, and Training. For AEO teams, the important change is that crawler policy can no longer be a blunt "allow AI" or "block AI" choice. Search visibility, agent task execution, and model training now need separate rules.

## What changed in July 2026

On July 1, 2026, Cloudflare announced [new AI traffic options for all customers](https://blog.cloudflare.com/content-independence-day-ai-options/). The new controls classify AI-related automation by purpose:

| Category | What it means | AEO implication |
|---|---|---|
| Search | Crawling or indexing content so it can be found later | Usually worth allowing for public discovery pages |
| Agent | User-directed automation that visits a site to complete a task | Needs action-safe UX, permissions, and error handling |
| Training | Crawling content to train or fine-tune models | Often needs a separate legal, licensing, or monetization decision |

Cloudflare says the options are available to all customers, including Free-tier users. That matters because crawler governance is moving from an enterprise-only control to a normal publishing decision.

## Why this matters for Agent Engine Optimization

Traditional SEO treated crawlers mainly as indexers. AEO has to treat automated visitors as different actors:

- a search crawler that helps users discover a page
- an answer engine that may quote or summarize the page
- a browser agent that may click, compare, or submit
- a training crawler that may absorb the content without sending traffic back

That is why [Agent Engine Optimization](/docs/what-is-aeo/) separates the [Read Layer](/docs/answer-engine-optimization/) from the [Execution Layer](/docs/execution-layer/). Search crawlers belong mostly to the read layer. Agent crawlers sit closer to execution.

## The September 15, 2026 default change

Cloudflare also announced a scheduled default change for new domains onboarding to Cloudflare on September 15, 2026. For ad-supported pages, Training and Agent categories will be blocked by default, while Search will remain allowed by default.

The detail AEO teams should not miss: multi-purpose crawlers can be affected by the most restrictive selected rule. Cloudflare explicitly notes that crawlers combining Search with Training may be blocked when a site owner chooses to block Training.

That creates a real SEO risk. A publisher can intend to block training but accidentally restrict a crawler that also supports search discovery.

## Recommended crawler policy by page type

| Page type | Search | Agent | Training | Notes |
|---|---:|---:|---:|---|
| Public homepage | Allow | Usually allow | Decide by business model | Keep the brand discoverable |
| Product pages | Allow | Allow with rate limits | Usually restrict or license | Product data must be current |
| Documentation | Allow | Allow | Decide | Agents need docs to complete tasks |
| Checkout | Restrict | Allow only with strong controls | Block | Payment and identity rules matter |
| Paid research | Maybe allow snippets | Restrict | Block or monetize | Consider summaries and gated detail |
| Internal tools | Block | Auth only | Block | No public crawler value |

This should be paired with [AI Crawlers and robots.txt](/docs/ai-crawlers-robots-txt/) and [Cloudflare AI Crawl Control](/docs/cloudflare-ai-crawl-control/).

## Implementation checklist

1. List your high-value public page types.
2. Decide which pages need search discoverability.
3. Decide where user-directed agents should be allowed to act.
4. Separate training use from search use in policy language.
5. Review Cloudflare AI traffic controls if the site runs behind Cloudflare.
6. Audit whether existing firewall rules block known AI referrers or agents.
7. Monitor crawl volume and referrals after changing rules.

Do not copy a competitor's blocklist. A media site, SaaS documentation hub, ecommerce store, and API business have different exposure and monetization needs.

## AEO mistake to avoid

The biggest mistake is treating "AI crawler" as one intent. A browser agent trying to buy a product for a user is not the same as a training crawler taking content for model improvement. If both are blocked by one rule, the site may protect content but lose agent-assisted conversions.

## FAQ

### Should every site allow Search crawlers?

Most public sites should allow reputable Search crawlers on indexable pages. Exceptions include private, paid, legally restricted, or low-value URLs.

### Should Agent crawlers be allowed?

Only where the agent can complete safe, user-benefiting tasks. Read-only pages are simpler than carts, forms, account changes, or purchases.

### Is Training crawling bad for AEO?

Not automatically. Some brands may accept it for visibility or licensing reasons. Others may restrict it because it does not create direct referrals.

### Can blocking Training hurt SEO?

It can if a crawler has multiple purposes and the infrastructure applies the most restrictive category. Cloudflare's July 2026 update makes that risk more explicit.

## Sources

Primary source: [Cloudflare: Your site, your rules](https://blog.cloudflare.com/content-independence-day-ai-options/). Related implementation context: [Cloudflare AI Crawl Control docs](https://developers.cloudflare.com/ai-crawl-control/).
