---
title: "Agent Access and Identity: Distinguishing and Verifying AI Agents"
metaTitle: "Agent Access and Identity: Web Bot Auth and RFC 9421"
description: "How websites recognize cryptographically signed agents like ChatGPT Dots, configure bot protections, and assign dedicated agent identities."
summary: "Analysis of agent access and identity: Web Bot Auth, Cloudflare Personal Agents policies, ChatGPT Wallet, and dedicated agent credentials."
keywords:
  - "agent access"
  - "agent identity"
  - "Web Bot Auth"
  - "RFC 9421"
  - "Cloudflare Personal Agents"
  - "ChatGPT Dots"
date: 2026-11-22
weight: 202
category: "Security"
---

# Agent Access and Identity: Distinguishing and Verifying AI Agents

Websites face a new architectural dilemma: modern bot protection must prevent scraping, denial-of-service, and automated exploitation, yet aggressively blocking all automated traffic will lock out paying customers whose purchases are transacted via autonomous personal agents.

Securing agent access requires cryptographic verification, granular edge policies, and establishing dedicated agent identities rather than reusing brittle employee logins.

> **Research Status:** November 22, 2026. All metrics, post timestamps (Europe/Berlin), and provider statements represent verified research data.

---

## Current Industry Developments (November 22, 2026)

### 1. ChatGPT Wallet Forces Merchants to Permit Signed Agents
OpenAI explicitly mandates that site firewalls do not block personal browser agents acting on behalf of users. OpenAI documentation instructs administrators on configuring Cloudflare: under **Personal Agents**, set the entry **"dots, OpenAI"** to **Allow (do not block)**. Alternatively, merchants can deploy a WAF custom rule targeting Bot Detection ID `129220581` (ChatGPT Operator).

- **Social Announcement:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), November 13, 2026, 17:44 Europe/Berlin (~1M impressions as of November 22, 2026).
- **Primary Sources:** [OpenAI, Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/), [OpenAI, Introducing Dots](https://openai.com/index/introducing-dots/), and [OpenAI, Help ensure cloud browser access to your site](https://developers.openai.com/commerce/agent-access).
- **Cryptographic Protocol:** Implementation relies on Web Bot Auth and [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) HTTP Message Signatures with headers `Signature`, `Signature-Input`, and `Signature-Agent` (`"https://chatgpt.com"`), resolving public keys via `https://chatgpt.com/.well-known/http-message-signatures-directory`.

### 2. Granular Policy Controls for Personal Agents on Cloudflare
As of November 4, 2026, webmasters can control supported personal agents individually with granular actions (**Allow**, **Block**, or **Block on pages with ads**). By default, personal agents inherit a site's overarching AI agent policy.

- **Changelog:** [Granular access controls for the top Personal Agents, November 4, 2026](https://developers.cloudflare.com/changelog/post/2026-11-04-personal-agent-policies/)
- **Technical Blog:** [See the agents, set the terms, November 4, 2026](https://blog.cloudflare.com/personal-agents-visibility-control/)
- **Documentation:** [AI Crawler and Agent access policies](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/) and [Web Bot Auth at Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/).

### 3. Signatures Prove the Operator, Not the Customer
Cryptographic validation under Web Bot Auth confirms that an HTTP request originated from an infrastructure operator (such as OpenAI), but it does not authenticate the specific end-user behind the request nor prove whether a specific action was authorized. To close this gap, Cloudflare introduced its "Trusted Agent Delegation" initiative.

- **Technical Analysis:** [Agents aren't humans (but they kinda are), November 5, 2026](https://blog.cloudflare.com/trusted-agent-delegation/)
- **Reference Post:** [@Cloudflare](https://x.com/Cloudflare/status/2118392403874701407), November 5, 2026, 18:18 Europe/Berlin
- **Standards Track:** IETF draft [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) and [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421).

### 4. Dedicated Agent Identities vs. Borrowed Corporate Credentials
Identity and Access Management (IAM) providers increasingly treat autonomous agents as distinct identity principals rather than service accounts or borrowed human logins.

- **Risk of Shared Logins:** [@Cloudflare](https://x.com/Cloudflare/status/2118288470275674172), November 5, 2026, 11:25 Europe/Berlin notes that when agents operate under employee credentials, audit logs become corrupted and actions appear under borrowed human names.
- **Enterprise Solutions:** [Okta on Agent Identity / CIMD](https://www.okta.com/blog/product-innovation/okta-cimd-ai-agent-identity/) and [@okta](https://x.com/okta/status/2107909146351669528), October 7, 2026, 21:01 Europe/Berlin. Further implementations include [Auth0 for Agentic Apps](https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/) and [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities).

### 5. WorkOS Agent Vault Takes the Opposite Approach
In contrast to dedicated cryptographic agent principals, WorkOS Agent Vault allows human users to deposit existing session credentials for agents to log in on their behalf.

- **Documentation & Stance:** [WorkOS Agent Vault Documentation](https://workos.com/docs/agent-vault) and [WorkOS Agent Vault Launch Blog](https://workos.com/blog/agent-vault).

---

## Planned In-Depth Articles (Coming Soon)

- *Web Bot Auth Explained: How to Verify Signed Agents like ChatGPT Dots* (Coming Soon)
- *Tuning Bot Management: Welcoming Paying Agents Without Dropping Shields* (Coming Soon)
- *Dedicated Agent Identities vs. Borrowed Corporate Logins* (Coming Soon)
- *The Signature Proves the Operator, Not the Customer: Understanding Delegation* (Coming Soon)
- *Step-by-Step Guide: Configuring Cloudflare Personal Agent Rules* (Coming Soon)
