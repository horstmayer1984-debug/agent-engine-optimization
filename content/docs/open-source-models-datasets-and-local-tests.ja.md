---
title: "AEO検証のためのモデル、データセット、ローカル実行環境"
metaTitle: "AEOローカル検証向けモデル・データセット（2026年）"
description: "AEO検証用オープンソース埋め込み、リランカー、ローカルLLM（Qwen3、MLX、llama.cpp）、学術ベンチマーク（GEO-bench、Mind2Web）の解説。"
summary: "AEOローカル検証環境の構築：多言語埋め込み、ニューラルリランカー、Apple Silicon向け量子化モデル、評価データセット。"
keywords:
  - "AEOモデル"
  - "Qwen3"
  - "bge-m3"
  - "llama.cpp"
  - "MLX"
  - "GEO-bench"
  - "Mind2Web"
date: 2026-11-22
weight: 214
category: "オープンソース"
---

# AEO検証のためのモデル、データセット、ローカル実行環境

AIエージェントが自社サイトをどう理解・抽出するかを検証するために、外部クラウドAPIに依存せず、オープンソースモデルを用いてローカル環境で決定論的テストを実施できます。

> **調査基準日:** 2026年11月22日。GitHub公式API取得データ。Hugging Faceのダウンロード数は調査対象外のため記載を省略。

---

## 1. セマンティック適合性テスト用埋め込みモデル
- **[Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B):** 多言語での高精度な意味検索・適合性測定。
- **[bge-m3](https://huggingface.co/BAAI/bge-m3):** 密結合・疎結合両対応の業界標準多言語モデル。
- **[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B):** 軽量で高速なローカル事前検証用。

---

## 2. パッセージ優先度を測るリランカー
- **[Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B):** 最終回答に採用されるパッセージ順位の検証。
- **[bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3):** 信頼性の高い多言語リランカー。
- **[jina-reranker-v3](https://huggingface.co/jinaai/jina-reranker-v3):** 高性能モデル。  
  *必須ライセンス表記:* **非商用利用限定（Non-commercial use only）**。商用サービスへの無断組み込みは不可。

---

## 3. ローカルLLMと実行ランタイム（例：Mac 64GBメモリ環境）
- **[Qwen3.8-27B MLX 8-bit](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit):** 重みサイズは約28GBと推定（*調査時の推定値*）。64GB RAMで広範なコンテキストを確保可能。
- **[Qwen3.6-35B-A3B GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF):** 高速なMoEバリアント。
- **[llama.cpp](https://github.com/ggml-org/llama.cpp):** C/C++製推論エンジン（MIT, 135,988スター, 最終更新 22.11.2026 09:08 Europe/Berlin）。
- **[mlx](https://github.com/ml-explore/mlx) / [mlx-lm](https://github.com/ml-explore/mlx-lm):** Apple Silicon向け最適化ランタイム。

---

## 4. 学術データセットとベンチマーク
- **[GEO-bench](https://huggingface.co/datasets/GEO-Optim/geo-bench):** GEO論文の公式評価データセット。
- **[Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web):** 実Webサイトを舞台としたエージェント評価データ。
- **[WebArena](https://github.com/web-arena-x/webarena):** Webタスク実行の検証環境（Apache-2.0, 1,645スター）。
