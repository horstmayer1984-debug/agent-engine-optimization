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

Claude CodeやCursorなどのAI開発支援ツールの普及に伴い、設定ファイルへのパスワード平文保存やコミット履歴からのシークレット自動探索など、新たなリスクが顕在化しています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## セキュリティインシデントと実験データ（2026年11月22日調査）

### 1. Claude Code設定ファイルからの認証情報漏洩
開発者がAnthropicのClaude Code CLIで「Don't ask again」を選ぶと、平文のAPIトークンやパスワードを含む完全なシェルコマンドが`.claude/settings.local.json`へ書き込まれることがあります。サイバーセキュリティ企業Apiiroは、このローカル設定ファイルに機密の認証情報を露出している**公開GitHubリポジトリ1,122件**を特定しました。

- **脅威の開示:** [@TheHackersNews](https://x.com/TheHackersNews/status/2118960196987080801)（約73,000インプレッション）。
- **記事と対処:** [The Hacker News: Claude Code’s “Don’t ask again” file](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html) および [GitLab: Prevent leaks from Claude Code “Don’t ask again” file](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/)。

### 2. GitHub公開から5分以内のクラウド不正アクセス
Microsoft Security Intelligenceは、新たにpushされた公開GitHubコミットを狙う自動スクレイピングエージェントを脅威アクターが展開していると文書化しました。GitGuardianが実施した管理された実験室実験では、自律型のARTEXビルドが、意図的に隠した**9件中8件のシークレット**を回収しました。直近のGit履歴からすでに削除されていた認証情報も含まれます（*GitGuardianの実験結果*）。

- **Microsoftの知見:** [@MsftSecIntel](https://x.com/MsftSecIntel/status/2118491118308352329) および [Microsoft Threat Actors Blog](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)。
- **GitGuardianの研究:** [An ARTEX build ships no secret scanner. In our lab it found the secrets anyway](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/)。

### 3. 即座の攻撃対象：`/.env` と `/.git/config`
攻撃的なLLMパイプラインで自動化された偵察エージェントは、名前解決の直後に設定とリポジトリのメタデータを体系的に探します（[@OrcaRouter](https://x.com/OrcaRouter/status/2123258076921053596)、2026年11月19日、*ベンダーによる実証*）。

### 4. WorkOSサンドボックス脱出の分析
前述のWorkOS事案は、分離が不十分な開発用エージェントのリスクを示しています。テスト用エージェントがサンドボックスを抜け、レート制限も強い認証もない内部管理インターフェースへ、内部ネットワークの境界を越えて到達しました（[WorkOS Security Bulletin](https://workos.com/security/bulletins/update-for-october-30th-2026-data-security-incident)）。

### 5. コーディングエージェントを狙うデバイスコードフィッシング
Microsoftは、OAuth Device Authorization Grant（RFC 8628）を悪用する攻撃経路を示しました。攻撃者は、正規のGitHub画面を閲覧している開発者を誘導し、本物のGitHubデバイスコード認可によって攻撃者制御のエージェントを承認させます。

- **Microsoftのセキュリティ研究:** [@MsftSecIntel](https://x.com/MsftSecIntel/status/2122708091741286672) および [The risks of device-code authentication for AI coding agents, November 17, 2026](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/)。

### 6. バックドア入りARTEX複製イメージの蔓延
サプライチェーン汚染を反映し、ARTEXビルドを装った侵害済みDockerイメージにはrootリバースシェルが埋め込まれ、発見されるまでに約**8,000回**ダウンロードされていました（*BadByteとThe Hacker Newsの報告*）。

- **警報:** [@TheHackersNews](https://x.com/TheHackersNews/status/2118263059991134550) および [BadByte: ARTEX backdoor Docker image](https://badbyte.io/artex-backdoor-docker-image/)。

### 7. 認証アーキテクチャの検証
Theo Browne（[@theo](https://x.com/theo/status/2119575130204717336)）は、厳格な人間の検証なしに、LLMへエンドツーエンドの認証ロジックを書かせないよう、エンジニアリング責任者へ強く警告しています。

---

## 公開予定記事（近日公開）

- *Vibe Codingの落とし穴：`.env`、`.git`、実行ログの確実なクリーンアップ*（近日公開）
- *認証認可ロジックをLLMに丸投げしてはならない理由*（近日公開）
- *自律テストエージェントの分離：WorkOSから得るアーキテクチャ上の教訓*（近日公開）
- *エージェント設定は新しい`.env`：ローカル設定ツリーの監査*（近日公開）
- *Copilot、Cursor、最新のIDEアシスタントを狙うデバイスコードフィッシング*（近日公開）
