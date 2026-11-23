---
title: "AI時代のセキュア開発：コーディングエージェントと認証情報の保護"
metaTitle: "セキュアAI開発：シークレット漏洩防止とエージェント保護"
description: "AIコーディングツールによる認証情報の漏洩、テスト環境の分離、デバイスコードフィッシング、バックドア付きフォークの危険性。"
summary: "AI支援開発におけるセキュリティ分析：Claude Code設定ファイル漏洩、GitGuardian実験、デバイスコードフィッシング。"
keywords:
  - "セキュア開発"
  - "コーディングエージェント"
  - "Claude Code設定漏洩"
  - "GitGuardian検証"
  - "デバイスコードフィッシング"
date: 2026-11-22
weight: 207
category: "セキュリティ"
---

# AI時代のセキュア開発：コーディングエージェントと認証情報の保護

Claude CodeやCursorなどのAI開発支援ツールの普及に伴い、設定ファイルへのパスワード平文保存やコミット履歴からのシークレット自動探索など、新たなリスクが顕在化しています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## セキュリティインシデントと実験データ（2026年11月22日調査）

### 1. Claude Code設定ファイルからの認証情報漏洩
Apiiroの調査により、「Don't ask again」を選択したことで`.claude/settings.local.json`内に平文トークンが保存され、公開GitHubリポジトリに流出した事例が**1,122件**確認されました（[The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html), [GitLab Blog](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/)）。

### 2. GitHub公開から5分以内のクラウド不正アクセス
GitGuardianの実験では、ARTEXエージェントが過去に削除されたGit履歴を含め、意図的に隠蔽された9件中**8件のシークレットを自動発見**しました（**GitGuardian実験データ**, [GitGuardian Blog](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/), [Microsoft Threat Blog](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)）。

### 3. コーディングエージェントを狙うデバイスコードフィッシング
攻撃者がGitHubの正規デバイス認可画面を偽装し、開発者に悪意あるエージェントを承認させる攻撃手法（[@MsftSecIntel](https://x.com/MsftSecIntel/status/2122708091741286672), [Microsoft Research](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/)）。

### 4. バックドア入りARTEX複製イメージの蔓延
悪意あるrootリバースシェルが仕込まれたDockerイメージが約8,000回ダウンロードされた事例（[BadByte](https://badbyte.io/artex-backdoor-docker-image/)）。

---

## 公開予定記事（近日公開）

- *Vibe Codingの落とし穴：`.env`、`.git`、実行ログの確実なクリーンアップ*（近日公開）
- *認証認可ロジックをLLMに丸投げしてはならない理由*（近日公開）
