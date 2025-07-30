#!/bin/bash

# Canva MCP を使った画像自動生成スクリプト

set -e

# 色付き出力用の関数
print_info() {
    echo -e "\033[34mℹ️  $1\033[0m"
}

print_success() {
    echo -e "\033[32m✅ $1\033[0m"
}

print_error() {
    echo -e "\033[31m❌ $1\033[0m"
}

print_warning() {
    echo -e "\033[33m⚠️  $1\033[0m"
}

# 引数チェック
if [ $# -eq 0 ]; then
    print_error "使用方法: $0 <記事名>"
    echo "利用可能な記事:"
    echo "  - ai-think-tag-monitoring"
    exit 1
fi

ARTICLE_NAME=$1

print_info "記事用画像生成開始: $ARTICLE_NAME"

# Pythonスクリプトの存在確認
SCRIPT_PATH="generate-images.py"
if [ ! -f "$SCRIPT_PATH" ]; then
    print_error "スクリプトが見つかりません: $SCRIPT_PATH"
    exit 1
fi

# Python実行
print_info "Pythonスクリプトを実行中..."
python3 "$SCRIPT_PATH" "$ARTICLE_NAME"

if [ $? -eq 0 ]; then
    print_success "画像生成が完了しました！"
    
    # 生成された画像の確認
    DATE_STR=$(date +%Y-%m-%d)
    IMAGE_DIR="images/${DATE_STR}-${ARTICLE_NAME}"
    
    if [ -d "$IMAGE_DIR" ]; then
        print_info "生成された画像:"
        ls -la "$IMAGE_DIR"
        
        # Gitに追加
        print_info "Gitに画像を追加中..."
        git add "$IMAGE_DIR"
        git commit -m "Add images for article: $ARTICLE_NAME"
        
        print_success "画像がGitに追加されました！"
        print_info "GitHubにプッシュするには: git push"
    fi
else
    print_error "画像生成に失敗しました"
    exit 1
fi 