# Design Doc

このドキュメントは、プロジェクトの設計に関する情報を提供する。

## アーキテクチャ

基本的には、DDD+クリーンアーキテクチャを採用

```mermaid
flowchart TD
    controllers --> use_cases
    use_cases --> domains
    use_cases --> services
    services --> domains
    infrastructures --> domains
```

- controllers: コントローラ層 (gRPCのserviceを定義)
- use_cases: ユースケース層 (一つのユースケースを実現するためのビジネスロジック)
- domains: ドメイン層 (ドメインモデル、エンティティ、バリューオブジェクト、リポジトリ)
- services: サービス層 (ドメインサービス)
- infrastructures: インフラ層 (データベース、外部API、ファイルシステムなどのインフラストラクチャ)

## ディレクトリ構成

```mermaid
flowchart TD
    schema --> schema.proto(schema.proto)

    app --> domains
    app --> use_cases
    app --> services
    app --> infrastructures
    app --> controllers
    app --> tests
    app --> gen

    domains --> domainA
    domainA --> xxx_entity.py(xxx_entity.py)

    use_cases --> xxx_use_case.py(xxx_use_case.py)

    services --> xxx_service.py(xxx_service.py)

    infrastructures --> clients
    clients --> xxx_client_impl.py(xxx_client.py)
    infrastructures --> repositories
    repositories --> xxx_repository_impl.py(xxx_repository_impl.py)

    controllers --> xxx_service_impl.py(xxx_service_impl.py)

    tests --> e2e
    tests --> unit
```
