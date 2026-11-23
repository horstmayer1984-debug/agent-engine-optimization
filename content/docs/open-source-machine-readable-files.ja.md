---
title: "llms.txt向けオープンソースツールランキングと徹底比較"
metaTitle: "オープンソースllms.txtツールランキング（2026年）"
description: "llms.txtの生成・監査・カタログ化を担うオープンソースツールの厳選ランキング。AEO適合性、開発頻度、スター数で評価。"
summary: "llms.txt向け主要ツールの比較：claude-seo、OpenGSO、公式仕様、VitePress/Starlight用プラグイン、llms-txt-hub。"
keywords:
  - "llms.txt"
  - "claude-seo"
  - "OpenGSO"
  - "AEOツール"
  - "オープンソース"
date: 2026-11-22
weight: 209
category: "オープンソース"
---

# llms.txt向けオープンソースツールランキングと徹底比較

`/llms.txt`は、AIエージェントやLLMがサイトの全体構造と主要ドキュメントを素早く把握するための機械可読インデックスです。

> **調査基準日:** 2026年11月22日。GitHubスター数、ライセンス、更新日時は公式API取得データ。

---

## 比較ランキング：機械可読ファイル生成・監査ツール

| 順位 | ツール名 | カテゴリ | AEOへの実用価値 | ライセンス | スター数 (22.11.2026) | 最終更新 (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Claude Code用スキル | 開発環境内でGEO、AEO、エージェント対応度を即座に監査。 | MIT | 31,471 | 16.11.2026, 07:16 |
| **2** | [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) | 監査・生成ツール | サイトをスコア化（0〜100）し、`llms.txt`、`robots.txt`、Sitemapを一括生成。 | Apache-2.0 | 398 | 09.11.2026, 16:17 |
| **3** | [llms.txt仕様](https://github.com/AnswerDotAI/llms-txt) | 標準仕様リファレンス | 記載すべき標準文法・構造のリファレンス。[llmstxt.org](https://llmstxt.org/)。 | Apache-2.0 | 2,699 | 24.09.2026, 19:21 |
| **4** | [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) | VitePress用プラグイン | VitePress製ドキュメントから`llms.txt`を自動コンパイル。 | MIT | 418 | 10.11.2026, 15:20 |
| **5** | [starlight-llms-txt](https://github.com/delucis/starlight-llms-txt) | Starlight用プラグイン | Astro Starlight製ドキュメントから`llms.txt`を自動生成。 | MIT | 118 | 18.11.2026, 01:12 |
| **6** | [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) | 導入サイトカタログ | `llms.txt`を採用するサイトの収集・索引。 | NOASSERTION | 930 | 22.11.2026, 06:05 |

---

## 利用シーン別の推奨ツール

- **仕様理解:** 自作する前に必ず**[llms.txt公式仕様](https://github.com/AnswerDotAI/llms-txt)**を確認してください。
- **VitePress / Astro利用時:** プラグインを導入してビルド時に自動生成するのが最適です。
- **スコアリングと一括生成:** **[OpenGSO](https://github.com/sherwinvishesh/OpenGSO)**を活用してください。
- **Claude Codeユーザー:** **[claude-seo](https://github.com/AgriciDaniel/claude-seo)**で開発中に事前チェックが可能です。
