# このマイクロサービスの技術選定

Date: 2025-05-19 JST

## Status

- Accepted

## Decision

技術選定として、以下を採用する

マイクロサービス間通信
- gRPC + protobuf

言語
- Python 3.13

使用ライブラリ

- Agent Development Kit (ADK)
- grpcio-tools

その他ツール

- uv
- ruff
- mypy
- buf

## Context

- マイクロサービス間通信は、レイテンシ・スループットに優れるgRPCを採用し、そのスキーマには、型定義に優れるprotobufを採用した
- Pythonは、LLMの関連ライブラリの数が多いため、採用した
- ADKは、LiteLLMによる複数LLMプロバイダーの対応、MCPのデフォルト対応という要件を満たしているため、採用した
- grpcio-toolsは、grpcのデフォルトのPython実装であるため、採用した
- uvは、pythonの依存関係を効率的に管理できるため、採用した
- ruffは、pythonの静的解析ツールであり、高速に動作するため、採用した
- mypyは、pythonの型チェックツールであり、型安全性を高めるため、採用した
- bufは、protobufのスキーマ管理ツールであり、スキーマのバージョン管理・コード生成を容易にするため、採用した

# 依存性注入ライブラリの選定

Date: 2025-05-19 JST

## Status

- Accepted

## Decision

依存性注入（DI）ライブラリとして、`dependency_injector` を採用する。

## Context

- PythonのDIライブラリには主に `dependency_injector` と `injector` がある
- `dependency_injector` は型安全性・補完性、構成管理、スコープ管理、設定ファイル連携、テスト容易性など、実運用に必要な機能が豊富
- ドキュメントや事例も多く、パフォーマンスも良い
- `injector` はシンプルだが、機能が最小限であり、型ヒントや補完もやや弱い
- 本プロジェクトはgRPCや外部API連携、テスト容易性、将来的な拡張性を重視するため、`dependency_injector` を採用する
