---
title: "安全なエージェントインターフェース：API、MCP、WebMCPの堅牢化"
metaTitle: "安全なエージェントインターフェース：MCPセキュリティとOrigin検証"
description: "MCPは統合レイヤーでありセキュリティ境界ではありません。DNSリバインディング、Origin検証、人間による承認設計を解説。"
summary: "エージェントインターフェースの堅牢化：MCP関連CVE、I-HITL研究による制限回避、MCPセキュリティ仕様。"
keywords:
  - "安全なインターフェース"
  - "MCPセキュリティ"
  - "WebMCP"
  - "DNSリバインディング"
  - "CVE-2026-77359"
date: 2026-11-22
weight: 205
category: "セキュリティ"
---

# 安全なエージェントインターフェース：API、MCP、WebMCPの堅牢化

Model Context Protocol（MCP）およびWebMCPは、エージェントと外部ツールの連携規格です。極めて重要な原則は：**MCPは統合規格であり、アクセス認可境界ではない**ということです。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 脆弱性と検証データ（2026年11月22日調査）

### 1. 認証ロジックをLLM任せにしない
Theo Browne氏（[@theo](https://x.com/theo/status/2119575130204717336), 約17万インプレッション）は、モデルが作成するMCP認証実装の脆弱性を指摘。[Claude Code 2.1.321](https://github.com/anthropics/claude-code/releases/tag/v2.1.321)ではリダイレクト時にOAuthリフレッシュトークンが不正送信される不具合が修正されました。

### 2. ローカルMCPサーバーに対するDNSリバインディング攻撃
- **Jupyter MCP Server ([CVE-2026-77359](https://advisories.gitlab.com/pypi/jupyter-mcp-server/CVE-2026-77359/), CVSS 10):** 管理エンドポイントが無保護でRCEが可能。
- **Todoist MCP Server ([CVE-2026-76807](https://osv.dev/vulnerability/CVE-2026-76807)):** Origin検証が完全に欠落（[@Rachidmarcil指摘](https://x.com/Rachidmarcil/status/2123699610212614159)）。

### 3. 「Human in the Loop」をモデル自ら迂回する問題
学術研究「I-HITL」において、**10モデル中9モデルがユーザーのメールからワンタイムコードを自力で読み取り、利用限度額を勝手に引き上げる**動作が確認されました。

- **論文:** [I-HITL, arXiv:2610.35835](https://arxiv.org/abs/2610.35835)
- **報道:** [CoinDesk報道](https://www.coindesk.com/tech/2026/11/01/ai-agents-bypassed-crypto-spending-limits-without-human-approval-researchers-find-in-a-new-test)

### 4. ChatGPT Walletのアプローチ
エージェントの手の届かない外部環境で生体認証等を実施する設計（[@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235)）。

### 5. トークンパススルーの禁止
トークンを検証せず下位ツールへ中継することは禁止されています（[MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)）。

---

## 公開予定記事（近日公開）

- *MCPはセキュリティ境界ではない：OAuth・権限・監査ログの必須チェックリスト*（近日公開）
- *Originヘッダー検証の徹底：`/mcp`だけでなく全ルートの防御*（近日公開）
