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
