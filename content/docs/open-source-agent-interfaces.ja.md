---
title: "MCP、WebMCP、エージェントブラウザ：重要リポジトリ徹底ランキング"
metaTitle: "MCP・WebMCP・エージェントブラウザ主要リポジトリ（2026年）"
description: "エージェント実行・連携のための主要オープンソースランキング：browser-use、Playwright MCP、Firecrawl MCP、WebMCPなど。"
summary: "AEO実行レイヤーの主要ツール比較：ブラウザ検証、MCPサーバー、W3C WebMCP仕様、開発SDK。"
keywords:
  - "browser-use"
  - "Playwright MCP"
  - "Firecrawl MCP"
  - "WebMCP"
  - "AEO実行レイヤー"
date: 2026-11-22
weight: 212
category: "オープンソース"
---

# MCP、WebMCP、エージェントブラウザ：重要リポジトリ徹底ランキング

従来のSEOがテキスト閲覧にとどまっていたのに対し、AEOでは**実行レイヤー（Execution Layer）**が重要になります。エージェントがサイト内を巡回し、フォームを入力し、APIを実行できるかが問われます。

> **調査基準日:** 2026年11月22日。GitHub公式API取得データ。

---

## 比較ランキング：エージェントインターフェースおよびブラウザ自動化

| 順位 | ツール名 | カテゴリ | AEOへの実用価値 | ライセンス | スター数 (22.11.2026) | 最終更新 (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [browser-use](https://github.com/browser-use/browser-use) | エージェントブラウザ | AIエージェントが実際にサイト内をクリック・操作する挙動を検証。 | MIT | 121,711 | 22.11.2026, 04:44 |
| **2** | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 公式MCPサーバー (MS) | Playwrightによるブラウザ制御を標準MCPツールとして提供。 | Apache-2.0 | 39,988 | 18.11.2026, 19:50 |
| **3** | [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | 公式MCPサーバー | Firecrawlの抽出・Markdown化機能をMCPクライアントへ提供。 | MIT | 7,880 | 22.11.2026, 06:53 |
| **4** | [WebMCP](https://github.com/webmachinelearning/webmcp) | W3C草案 | サイト自身がブラウザ内エージェントへ直接ツールを公開する新規格。 | 要リポジトリ確認 | 5,010 | 22.11.2026, 02:23 |
| **4b** | [webmcp-tools](https://github.com/GoogleChromeLabs/webmcp-tools) | Chrome Labs開発ツール | WebMCP Origin Trialを支援するChrome Labs公式ツール群。 | Apache-2.0 | 796 | 20.11.2026, 19:15 |
| **5** | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 公式Python SDK | 独自AEOツールやMCPサーバー構築のための標準開発キット。 | MIT | 24,929 | 17.11.2026, 10:38 |
| **6** | [NLWeb](https://github.com/nlweb-ai/NLWeb) | 会話型Webレイヤー | サイトを対話可能にする試み。*2026年8月以降コミット停止。* | MIT | 6,262 | 11.08.2026, 21:35 |
| **7** | [fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) | 候補MCPサーバー | 簡易的なWebフェッチ・テスト用サーバー。 | MIT | 1,088 | 05.11.2026, 06:53 |

---

## ツール選定の指針

- **エージェント視点での導線テスト:** **[browser-use](https://github.com/browser-use/browser-use)**または**[Playwright MCP](https://github.com/microsoft/playwright-mcp)**を採用。
- **独自MCPツールの開発:** 公式**[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)**を使用。
- **注意点:** **NLWeb**は2026年8月11日以降コミットが停止している点に留意してください。
