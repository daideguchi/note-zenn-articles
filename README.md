# Note・Zenn 投稿管理ルール

## 📁 ディレクトリ構成

```
note/
├── README.md (このファイル)
├── drafts/          # 下書き
├── published/       # 公開済み記事
├── images/          # 記事用画像
├── templates/       # 記事テンプレート
└── scripts/         # 自動化スクリプト
    ├── generate-images.py
    ├── run-image-generation.sh
    └── canva-mcp-config.json
```

## 📝 記事作成ルール

### 1. ファイル命名規則

- 形式: `YYYY-MM-DD-記事タイトル.md`
- 例: `2024-01-15-ai-think-tag-monitoring.md`
- 日本語タイトルは英語に変換

### 2. マークダウン記法ルール

#### ✅ 使用可能

- `# ## ###` 見出し
- `**太字**` `*斜体*`
- `- リスト`
- `| テーブル |`
- `[リンク](URL)`
- `![画像](URL)`
- `コードブロック`
- `---` 区切り線

#### ❌ 使用禁止

- `>` 引用ブロック（note で「出典を入力」表示される）
- 複雑な HTML タグ
- 特殊なマークダウン拡張記法

### 3. 記事構造テンプレート

```markdown
# 記事タイトル

## 要旨

記事の要点を簡潔にまとめる

## 本文

### セクション 1

内容...

### セクション 2

内容...

## まとめ

記事の結論

---

**✍️ この記事は Zenn／Note／Qiita などにそのまま転載 OK。ご自由にコピペしてお使いください！**
```

## 🖼️ 画像挿入について

### Git + マークダウンでの画像表示

**✅ 可能です！** 以下の方法で画像を表示できます：

#### 方法 1: GitHub Raw URL 使用

```markdown
![画像説明](https://raw.githubusercontent.com/ユーザー名/リポジトリ名/main/note/images/画像名.png)
```

#### 方法 2: GitHub Pages 使用（推奨）

1. GitHub Pages を有効化
2. 以下の URL 形式で画像を挿入：

```markdown
![画像説明](https://ユーザー名.github.io/リポジトリ名/note/images/画像名.png)
```

### 🎨 Canva MCP を使った画像自動生成

#### セットアップ

1. **Canva MCP サーバーをインストール**

   ```bash
   # Cursor で MCP サーバーをインストール済み
   # @modelcontextprotocol/server-canva
   ```

2. **Canva アクセストークンを設定**
   ```bash
   # canva-mcp-config.json にトークンを設定
   ```

#### 画像自動生成

```bash
# 記事用画像を自動生成
./scripts/run-image-generation.sh ai-think-tag-monitoring
```

#### 生成される画像

- **メイン画像** (1200x630px): 記事サムネイル
- **フローチャート** (800x600px): 欺瞞検出プロセス
- **ダイアグラム** (800x600px): think タグ構造

### 画像管理ルール

#### ディレクトリ構成

```
note/images/
├── 2024-01-15-ai-think-tag/  # 記事別フォルダ
│   ├── demo-screenshot.png
│   └── diagram.png
└── common/                   # 共通画像
    ├── logo.png
    └── icons/
```

#### 画像ファイル命名

- 形式: `記事日付-画像説明.拡張子`
- 例: `2024-01-15-think-tag-demo.png`
- 英数字・ハイフンのみ使用

#### 推奨画像形式

- **PNG**: スクリーンショット、図表
- **JPG**: 写真
- **SVG**: アイコン、ロゴ（可能な場合）
- **WebP**: 軽量化したい場合

### 画像最適化

#### サイズ制限

- **note**: 最大 10MB
- **Zenn**: 最大 5MB
- **推奨**: 1MB 以下

#### 解像度

- **スクリーンショット**: 1200px 幅程度
- **図表**: 800px 幅程度
- **アイコン**: 200px 幅程度

## 🔄 投稿ワークフロー

### 1. 記事作成

```bash
# 1. 下書き作成
cp templates/article-template.md drafts/2024-01-15-記事タイトル.md

# 2. 画像準備（自動生成）
./scripts/run-image-generation.sh 記事名

# 3. 記事執筆
# drafts/ 内で編集
```

### 2. レビュー・修正

- マークダウン記法チェック
- 画像表示確認
- リンク切れチェック

### 3. 公開

```bash
# 1. 公開用に移動
mv drafts/2024-01-15-記事タイトル.md published/

# 2. Gitにコミット
git add .
git commit -m "Add article: 記事タイトル"
git push

# 3. note/Zennにコピペ
```

## 📋 チェックリスト

### 記事公開前チェック

- [ ] ファイル名が命名規則に従っている
- [ ] 引用ブロック（`>`）を使用していない
- [ ] 画像パスが正しい
- [ ] リンクが有効
- [ ] テーブルが正しく表示される
- [ ] コードブロックに言語指定がある
- [ ] 最後に転載許可コメントがある

### 画像チェック

- [ ] ファイルサイズが制限内
- [ ] 解像度が適切
- [ ] ファイル名が英数字のみ
- [ ] GitHub Raw URL または Pages URL を使用

## 🚀 自動化 Tips

### GitHub Actions で画像最適化

```yaml
# .github/workflows/optimize-images.yml
name: Optimize Images
on: [push]
jobs:
  optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: calibreapp/image-actions@main
        with:
          githubToken: ${{ secrets.GITHUB_TOKEN }}
          compressOnly: true
```

### 画像一括リサイズ

```bash
# ImageMagick使用例
find note/images -name "*.png" -exec convert {} -resize 1200x {} \;
```

## 📚 参考リンク

- [Note マークダウン記法](https://note.com/help/articles/markdown)
- [Zenn マークダウン記法](https://zenn.dev/zenn/articles/markdown-guide)
- [GitHub Pages 設定](https://docs.github.com/ja/pages/getting-started-with-github-pages)
- [GitHub Raw URL](https://docs.github.com/ja/repositories/working-with-files/using-files/viewing-a-file)
- [Canva MCP サーバー](https://github.com/modelcontextprotocol/server-canva)

---

**💡 このルールに従えば、note・Zenn・Qiita など、どのプラットフォームでも同じマークダウンが使えます！**
