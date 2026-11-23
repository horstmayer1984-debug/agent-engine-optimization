---
title: "AIエージェントアクセスの検知と検証：主要オープンソースランキング"
metaTitle: "AIエージェントトラフィック分析・検証ツール（2026年）"
description: "AIエージェントのアクセス識別・署名検証ツールのランキング：Web Bot Auth、AgentCake、mintlify/agent-trafficなど。"
summary: "エージェントアクセスの識別実践：RFC 9421署名検証、セッションリプレイ分析、トラフィック分類、適合性テスト。"
keywords:
  - "Web Bot Auth"
  - "AgentCake"
  - "mintlify agent-traffic"
  - "エージェント検証"
date: 2026-11-22
weight: 213
category: "オープンソース"
---

# AIエージェントアクセスの検知と検証：主要オープンソースランキング

AIエージェントによるアクセスは、従来のWeb解析ツールでは正しく判定できません。署名の暗号検証やエージェント専用の行動ログ分析が不可欠です。

> **調査基準日:** 2026年11月22日。GitHub公式API取得データ。

---

## 比較ランキング：エージェント識別・トラフィック解析

| 順位 | ツール名 | カテゴリ | AEOへの実用価値 | ライセンス | スター数 (22.11.2026) | 最終更新 (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [Web Bot Auth](https://github.com/cloudflare/web-bot-auth) | 署名検証 (RFC 9421) | リクエストが署名された正当なエージェント運営者からのものかを暗号的に検証。 | Apache-2.0 | 186 | 21.11.2026, 20:46 |
| **2** | [AgentCake](https://github.com/tartini-ai/agent-traffic-analytics) | トラフィック解析 / リプレイ | エージェントと人間のトラフィックを識別し、エージェント特有の動作をリプレイ。 | MIT | 91 | 21.11.2026, 15:03 |
| **3** | [mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) | トラフィック分類器 | 受信アクセスをエージェント、検索クローラー、人間に分類。 | MIT | 88 | 10.11.2026, 19:43 |
| **4** | [Botscent](https://github.com/nalinbhardwaj/botscent) | 検知ライブラリ | 行動パターンからエージェントを判定する軽量モジュール。 | MIT | 35 | 11.11.2026, 17:13 |
| **5** | [AgentReady](https://github.com/agentready-org/standard) | 適合性スキャナー | `npx is-agentic`によるエージェント対応度チェック。ライセンス未記載。 | API未記載 | 65 | 11.11.2026, 23:50 |

---

## ツール選定のアドバイス

- **確実な認証:** **[Web Bot Auth](https://github.com/cloudflare/web-bot-auth)**を用いてHTTP署名を検証します。
- **行動・分析:** **[AgentCake](https://github.com/tartini-ai/agent-traffic-analytics)**または**[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)**でエージェントトラフィックを可視化します。
