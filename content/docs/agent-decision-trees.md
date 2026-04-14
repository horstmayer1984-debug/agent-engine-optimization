---
title: "Deterministic Decision Trees: How AI Agents Evaluate Your Website Before Acting"
date: 2026-04-14
weight: 92
category: "Architecture"
description: "AI agents run strict pass/fail decision trees before transacting. Which deterministic questions they ask, what causes immediate exclusion, and how to pass every check."
summary: "Agents do not browse and decide intuitively. They execute deterministic decision trees with strict pass/fail criteria. Fail one check and the agent moves to a competitor."
keywords:
  - agent decision trees
  - deterministic agent evaluation
  - agent pass fail criteria
  - capability mapping agents
  - agent exclusion criteria
  - machine to machine evaluation
---

AI agents do not evaluate your website the way humans do. They do not browse, form impressions, and gradually build confidence. They execute deterministic decision trees with strict pass/fail criteria at each node. Fail one check and the process terminates. The agent moves to the next vendor without explanation.

Understanding these decision trees is the difference between being selected and being silently excluded.

## The six questions every agent asks

### Question 1: What can this system do?

The agent checks for a capability manifest. In UCP implementations, this is the JSON file at /.well-known/ucp. In MCP implementations, it is the tool and resource schemas returned by the server. In simpler setups, it is the llms.txt file or Agent Card.

If the agent cannot determine what your system supports, it skips you entirely. There is no partial credit. Either the capabilities are declared or they are not.

Pass condition: a machine-readable declaration of supported actions, data types, and transaction capabilities.

Fail condition: no manifest, no schema, no llms.txt. The agent has no way to determine what you offer.

### Question 2: Which inputs are required?

Once the agent knows what you can do, it checks whether it has the required inputs to trigger the action. Your system must provide a clear schema of expected input values: data types, required versus optional fields, validation rules, and acceptable ranges.

Pass condition: every endpoint or action has a documented input schema with types, constraints, and examples.

Fail condition: input requirements are vague, undocumented, or only discoverable by trial and error.

### Question 3: Is the current state verifiable?

The agent does not trust static page content. It needs to verify critical state in real time.

Is the price explicit and current? Human phrases like "price upon request" or "starting from" cause immediate exclusion in risk-averse transactions. The agent needs an exact number valid for a defined time window.

Is inventory verified in real time? The agent sends an API call. Cached HTML that says "in stock" is worthless if the actual inventory was depleted two hours ago.

Are policies structured and machine-readable? Return policies, shipping terms, cancellation conditions. If these exist only as prose paragraphs in a legal page, the agent cannot parse them reliably. Schema.org Action tags and structured policy declarations are required.

Pass condition: real-time verifiable state for every critical transaction parameter.

Fail condition: stale data, ambiguous pricing, unstructured policies, or any parameter that requires interpretation rather than parsing.

### Question 4: What state is guaranteed after the action?

The agent needs deterministic guarantees about what will happen when it acts. If it submits a purchase, will it receive a confirmation with an order ID? If it books an appointment, will it receive a confirmed time slot? If the action fails, will it receive a structured error explaining why?

Pass condition: every action endpoint returns a deterministic result (success with confirmation details or failure with specific error classification).

Fail condition: ambiguous responses, human-language confirmations without structured data, or endpoints that return success without verifiable proof.

### Question 5: Do attributes match across sources?

Agents cross-reference data from multiple sources. If your price in the Google Merchant Center differs from your API response, or your schema markup shows a different availability than your UCP manifest, the agent detects the inconsistency.

Inconsistencies do not just cause confusion. They cause exclusion. An agent that cannot trust your data will not transact through your system.

Pass condition: identical values for price, availability, specifications, and policies across all machine-readable sources (schema markup, API responses, product feeds, UCP manifest).

Fail condition: any discrepancy between data sources.

### Question 6: Is the action safely repeatable?

Agents retry on failure. If a network timeout occurs after submitting a purchase, the agent will send the same request again. Your system must handle this without creating duplicate orders, duplicate charges, or corrupted state.

Pass condition: idempotent transaction endpoints where the same request produces the same result regardless of how many times it is sent.

Fail condition: non-idempotent endpoints where retries create duplicates.

## The decision tree in practice

The agent evaluates these questions sequentially. Each "fail" terminates the evaluation immediately:

Capability declared? No → excluded. Inputs documented? No → excluded. State verifiable in real time? No → excluded. Outcomes deterministic? No → excluded. Data consistent across sources? No → excluded. Retries safe? No → excluded.

Only if all six checks pass does the agent proceed with the transaction.

## Why this differs from human evaluation

A human buyer tolerates ambiguity. "Price upon request" means they will call. "Usually ships in 3 to 5 days" is close enough. A confusing return policy gets skimmed and accepted.

An agent tolerates none of this. Every ambiguity is a fail condition. Every "usually" is indeterminate. Every unstructured policy is unparseable. The agent operates on binary logic: verified or excluded.

This is why sites that look polished to humans can score zero with agents. Visual design, brand reputation, and persuasive copy carry no weight in a deterministic decision tree.

The [execution layer guide](/docs/execution-layer/) explains the infrastructure requirements. The [AEO implementation guide](/docs/implement-aeo/) covers the step-by-step optimization path.

---

## FAQ

**What is a deterministic decision tree in AEO?**
A strict sequence of pass/fail checks that an agent executes before transacting with your site. Each check evaluates a specific requirement (capabilities, inputs, state, outcomes, consistency, idempotency). Failing any check causes immediate exclusion.

**What is the most common reason agents exclude a site?**
Unstructured or ambiguous pricing. "Price upon request," "starting from," or prices that differ between schema markup and API responses cause immediate exclusion.

**How do I test whether my site passes agent evaluation?**
Simulate the six questions manually. Can you find your capability declaration? Are all inputs documented? Can you verify state through an API call? Do all data sources return identical values? Run this check monthly.

**What is a capability manifest?**
A machine-readable file that declares what your system can do. In UCP: /.well-known/ucp. In MCP: tool and resource schemas. In simpler setups: llms.txt or agent-card.json.

**Why does idempotency matter so much?**
Because agents retry on failure. A timeout does not mean the action failed. If your endpoint creates a duplicate order on retry, the agent has caused real damage. Idempotent endpoints handle retries safely by returning the same result for the same request.
