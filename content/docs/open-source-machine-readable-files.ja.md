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

## ツール別の要点

### 1. claude-seo
- **焦点:** 開発ワークフローへの統合。
- **AEOで重要な理由:** Claude Code内の対話的な監査スキルとして組み込まれ、`claude-seo`は本番へpushする前に、ローカルのコード変更をGEO（Generative Engine Optimization）とAEOの観点で検証します。
- **リポジトリ:** [github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

### 2. OpenGSO
- **焦点:** 包括的な自動対応度監査。
- **AEOで重要な理由:** Webページ全体で決定論的な対応度スコア（0〜100）を出しつつ、妥当な`llms.txt`、`robots.txt`、XMLサイトマップを同時に組み立てます。
- **リポジトリ:** [github.com/sherwinvishesh/OpenGSO](https://github.com/sherwinvishesh/OpenGSO)

### 3. llms.txt仕様（AnswerDotAI）
- **焦点:** 基盤となる標準。
- **AEOで重要な理由:** 標準的なMarkdownセクション（`# Project Name`、`> Summary block`、OptionalとCoreのドキュメント）を定義します。独自の生成パイプラインを実装する前に必ず参照してください。
- **リポジトリ:** [github.com/AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt)

### 4. vitepress-plugin-llmsとstarlight-llms-txt
- **焦点:** 静的サイトジェネレーターへのネイティブ統合。
- **AEOで重要な理由:** VitePressとAstro Starlight向けの、設定ほぼ不要のプラグインです。通常のビルド手順の中で、ドキュメント階層を正規の機械可読エンドポイントへまとめます。
- **リポジトリ:** [github.com/okineadev/vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) および [github.com/delucis/starlight-llms-txt](https://github.com/delucis/starlight-llms-txt)

### 5. llms-txt-hub
- **焦点:** エコシステムの発見。
- **AEOで重要な理由:** 主要なオープンソースプロジェクトが公開`llms.txt`をどう構成しているかを観察する参照索引です。GitHubのライセンス欄は`NOASSERTION`である点に注意してください。
- **リポジトリ:** [github.com/thedaviddias/llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub)

---

## 利用シーン別の推奨ツール

- **仕様理解:** 自作する前に必ず**[llms.txt公式仕様](https://github.com/AnswerDotAI/llms-txt)**を確認してください。
- **VitePress / Astro利用時:** プラグインを導入してビルド時に自動生成するのが最適です。
- **スコアリングと一括生成:** **[OpenGSO](https://github.com/sherwinvishesh/OpenGSO)**を活用してください。
- **Claude Codeユーザー:** **[claude-seo](https://github.com/AgriciDaniel/claude-seo)**で開発中に事前チェックが可能です。
