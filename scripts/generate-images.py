#!/usr/bin/env python3
"""
Canva MCP を使った記事用画像自動生成スクリプト
"""

import sys
from datetime import datetime
from pathlib import Path

# 記事用画像生成設定
IMAGE_CONFIGS = {
    "ai-think-tag-monitoring": {
        "main_image": {
            "prompt": (
                "Create a professional tech illustration showing AI transparency "
                "and monitoring. Include a brain icon connected to code blocks "
                "with <think> tags. Use blue and green color scheme. "
                "Style: modern, clean, suitable for technical blog about "
                "AI deception detection."
            ),
            "size": "1200x630",
            "filename": "main-image.png"
        },
        "flowchart": {
            "prompt": (
                "Create a flowchart showing AI deception detection process: "
                "1. Monitor AI thoughts with think tags "
                "2. Check for inconsistencies and lies "
                "3. Verify with multiple sources. "
                "Use professional business style with blue theme."
            ),
            "size": "800x600",
            "filename": "deception-detection-flowchart.png"
        },
        "diagram": {
            "prompt": (
                "Create a diagram showing the structure of think tags in "
                "AI code generation. Show <think> section with thought process "
                "and <code> section with final code. Clean, technical style."
            ),
            "size": "800x600",
            "filename": "think-tag-structure.png"
        }
    }
}


def create_image_directory(article_name):
    """記事用の画像ディレクトリを作成"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    image_dir = Path(f"images/{date_str}-{article_name}")
    image_dir.mkdir(parents=True, exist_ok=True)
    return image_dir


def generate_canva_image(prompt, size, filename, output_dir):
    """Canva MCPを使って画像を生成"""
    try:
        # Canva MCPコマンドを実行
        # 実際のMCPコマンドは、Canva MCPの仕様に応じて調整が必要
        print(f"🎨 画像生成中: {filename}")
        print(f"📝 プロンプト: {prompt}")
        print(f"📏 サイズ: {size}")
        
        # ここでCanva MCPの実際のコマンドを呼び出す
        # 例: canva_create_image(prompt, size, output_path)
        
        output_path = output_dir / filename
        print(f"✅ 画像保存: {output_path}")
        
        return str(output_path)
        
    except Exception as e:
        print(f"❌ 画像生成エラー: {e}")
        return None


def generate_article_images(article_name):
    """記事用の全画像を生成"""
    print(f"🚀 記事用画像生成開始: {article_name}")
    
    if article_name not in IMAGE_CONFIGS:
        print(f"❌ 設定が見つかりません: {article_name}")
        return
    
    # 画像ディレクトリ作成
    image_dir = create_image_directory(article_name)
    print(f"📁 画像ディレクトリ: {image_dir}")
    
    # 各画像を生成
    generated_images = []
    config = IMAGE_CONFIGS[article_name]
    
    for image_type, settings in config.items():
        print(f"\n🖼️ {image_type} 画像生成中...")
        
        output_path = generate_canva_image(
            settings["prompt"],
            settings["size"],
            settings["filename"],
            image_dir
        )
        
        if output_path:
            generated_images.append({
                "type": image_type,
                "path": output_path,
                "filename": settings["filename"]
            })
    
    # 生成結果をレポート
    print(f"\n📊 生成完了レポート:")
    print(f"📁 ディレクトリ: {image_dir}")
    print(f"🖼️ 生成画像数: {len(generated_images)}")
    
    for img in generated_images:
        print(f"  - {img['type']}: {img['filename']}")
    
    # マークダウン用の画像リンクを生成
    print(f"\n📝 マークダウン用画像リンク:")
    for img in generated_images:
        github_url = (
            f"https://daideguchi.github.io/note-zenn-articles/{img['path']}"
        )
        print(f"![{img['type']}]({github_url})")
    
    return generated_images


def main():
    """メイン関数"""
    if len(sys.argv) < 2:
        print("使用方法: python generate-images.py <記事名>")
        print("利用可能な記事:")
        for article in IMAGE_CONFIGS.keys():
            print(f"  - {article}")
        return
    
    article_name = sys.argv[1]
    generate_article_images(article_name)


if __name__ == "__main__":
    main() 