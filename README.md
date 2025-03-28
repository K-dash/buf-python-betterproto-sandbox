# buf-python-betterproto-sandbox

このプロジェクトは、Buf CLI と python-betterproto プラグインを利用して生成された gRPC スタブコードを使用したサンプルアプリケーションです。

## 特徴

- **Buf CLI**  
  プロトコル定義（.proto ファイル）の管理やコード生成を行うために Buf CLI を使用

- **python-betterproto**  
  .proto ファイルから Python 用の gRPC スタブコードを生成するために、python-betterproto プラグインを利用

- **gRPC サーバ/クライアント**  
  生成されたコードを用いて、ペット情報を扱う gRPC サーバとクライアント間の通信のサンプルを実装

## ディレクトリ構成

```
proto/                          # プロトコル定義ファイル (.proto)
pet_service/
├── src/
│   ├── gen/                    # python-betterproto により生成されるコード
│   ├── services/
│   │   └── pet.py              # gRPC サービスの実装（PetStoreService）
│   ├── client.py               # gRPC クライアント実装
│   └── server.py               # gRPC サーバ実装
└── Makefile.toml               # cargo make によるタスク実行用ファイル（サーバ・クライアント起動）
```

## 前提条件

- Rust 製のタスクランナー `cargo make` がインストールされていることが前提です。
- Python 環境管理ツール `uv` が必要です。

## 使い方

### 1. 依存関係のセットアップ

プロジェクトのルートディレクトリにて、以下のコマンドで仮想環境を作成し、依存関係をインストールします。

```bash
cd pet_service
makers setup
```

### 2. プロトコル定義からのコード生成

Buf CLI と python-betterproto プラグインを使用して、.proto ファイルから Python コードを生成します。以下のコマンドで実行できます。

```bash
makers gen
```

### 3. gRPC サーバの起動

以下のコマンドで、gRPC サーバを起動します。  
サーバはデフォルトで `127.0.0.1:50051` で待ち受けます。

```bash
makers run-server
```

### 4. gRPC クライアントの実行

別のターミナルを開いて、以下のコマンドを実行し、サンプルクライアントからサーバへリクエストを送信します。

```bash
makers client

...
GetPetResponse(pet=Pet(pet_type=PetType.DOG, pet_id='1', name='Buddy', created_at=DateTime(year=2021, month=8, day=1, hours=12)))
```

クライアントは、指定した `pet_id` をもとにサーバからダミーのペット情報を受け取ります。

また、`buf curl` コマンドを使ってgRPCサーバーにリクエストを送信することもできます。

```bash
makers buf-curl

...
{
  "pet": {
    "petType": "PET_TYPE_DOG",
    "petId": "1",
    "name": "Buddy",
    "createdAt": {
      "year": 2021,
      "month": 8,
      "day": 1,
      "hours": 12
    }
  }
}
```

### 5. mypy の実行

mypy を使って proto ファイルから生成されたコード、および gRPC サーバー/クライアントの型チェックを実行します。

```bash
makers mypy
```
