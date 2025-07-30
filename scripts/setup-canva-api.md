# Canva Apps SDK セットアップ手順

## 🎯 推奨アプローチ

記事用画像自動生成には **Canva Apps SDK** を使用します。Connect APIs よりも適している理由：

- ✅ **リアルタイム画像生成**
- ✅ **高品質なデザイン機能**
- ✅ **ブラウザ内で直接実行**
- ✅ **ユーザーインターフェース付き**

## 📋 セットアップ手順

### 1. Canva 開発者アカウント作成

1. [Canva Developers](https://www.canva.com/developers/) にアクセス
2. 「Get Started」をクリック
3. 開発者アカウントを作成

### 2. アプリケーション作成

1. **Apps SDK** を選択
2. 新しいアプリケーションを作成
3. 以下の情報を設定：
   - **App Name**: `Note-Zenn-Image-Generator`
   - **Description**: `Automated image generation for tech articles`
   - **App Type**: `Design Editor`

### 3. 必要な権限設定

Apps SDK で必要な権限：

- `designs:read` - デザイン読み取り
- `designs:write` - デザイン作成・編集
- `assets:read` - アセット読み取り
- `assets:write` - アセットアップロード

### 4. 開発環境セットアップ

```bash
# Canva CLI インストール
npm install -g @canva/cli

# プロジェクト初期化
canva init note-zenn-image-generator
cd note-zenn-image-generator

# 開発サーバー起動
canva dev
```

### 5. 画像生成機能実装

Apps SDK の主要機能：

- **Creating images**: 画像作成
- **Creating shapes**: 図形作成
- **Creating text**: テキスト作成
- **Exporting designs**: デザインエクスポート

## 🚀 使用方法

### 画像生成コマンド

```bash
# 記事用画像を自動生成
./scripts/run-image-generation.sh ai-think-tag-monitoring
```

### 生成される画像

1. **メイン画像** (1200x630px)

   - AI 透明性・監視の概念図
   - 脳アイコン + コードブロック

2. **フローチャート** (800x600px)

   - 欺瞞検出プロセス
   - 3 段階の監視フロー

3. **ダイアグラム** (800x600px)
   - think タグ構造図
   - 思考プロセスとコード生成

## 📝 注意事項

- **無料利用**: Apps SDK は無料で利用可能
- **制限**: 月間 API 呼び出し数に制限あり
- **認証**: OAuth 2.0 認証が必要
- **セキュリティ**: Client Secret は絶対に公開しない

## 🔗 参考リンク

- [Canva Apps SDK Documentation](https://www.canva.dev/docs/apps/)
- [Quickstart Guide](https://www.canva.dev/docs/apps/quickstart/)
- [Creating Images](https://www.canva.dev/docs/apps/creating-images/)
- [Exporting Designs](https://www.canva.dev/docs/apps/exporting-designs/)
