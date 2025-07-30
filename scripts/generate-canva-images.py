#!/usr/bin/env python3
"""
Canva Apps SDKを使って実際に画像を生成するスクリプト
"""

import sys
import requests
import time
import json
from datetime import datetime
from pathlib import Path

# Canva Apps SDKの設定
CANVA_BACKEND_URL = "http://localhost:3001"  # デフォルトポート

# 記事別の画像設定
IMAGE_CONFIGS = {
    "ai-think-tag-monitoring": {
        "main_image": {
            "prompt": (
                "Create a professional tech illustration showing AI transparency and "
                "monitoring. Include a brain icon connected to code blocks with <think> "
                "tags. Use blue and green color scheme. Style: modern, clean, suitable "
                "for technical blog about AI deception detection."
            ),
            "size": "1200x630",
            "filename": "main-image.png",
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
            "filename": "deception-detection-flowchart.png",
        },
        "diagram": {
            "prompt": (
                "Create a diagram showing the structure of think tags in AI code "
                "generation. Show <think> section with thought process and <code> "
                "section with final code. Clean, technical style."
            ),
            "size": "800x600",
            "filename": "think-tag-structure.png",
        },
    }
}


def create_image_directory(article_name):
    """記事用の画像ディレクトリを作成"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    image_dir = Path(f"images/{date_str}-{article_name}")
    image_dir.mkdir(parents=True, exist_ok=True)
    return image_dir


def check_canva_server():
    """Canva Apps SDKサーバーが起動しているかチェック"""
    try:
        response = requests.get(f"{CANVA_BACKEND_URL}/api/credits", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def generate_canva_image(prompt, size, filename, output_dir):
    """Canva Apps SDKを使って画像を生成"""
    try:
        print(f"🎨 画像生成中: {filename}")
        print(f"📝 プロンプト: {prompt}")
        print(f"📏 サイズ: {size}")

        # 画像生成をキューに追加
        queue_url = f"{CANVA_BACKEND_URL}/api/queue-image-generation"
        params = {"prompt": prompt, "count": 1}

        response = requests.post(queue_url, params=params)
        if response.status_code != 200:
            print(f"❌ 画像生成キューエラー: {response.status_code}")
            return None

        job_data = response.json()
        job_id = job_data.get("jobId")

        if not job_id:
            print("❌ ジョブIDが取得できませんでした")
            return None

        print(f"🔄 ジョブID: {job_id}")

        # 画像生成完了を待機
        max_attempts = 30  # 最大30回試行
        attempt = 0

        while attempt < max_attempts:
            status_url = f"{CANVA_BACKEND_URL}/api/job-status"
            params = {"jobId": job_id}

            response = requests.get(status_url, params=params)
            if response.status_code == 200:
                status_data = response.json()

                if status_data.get("status") == "completed":
                    images = status_data.get("images", [])
                    if images:
                        # 最初の画像をダウンロード
                        image_url = images[0]["fullsize"]["url"]
                        output_path = output_dir / filename

                        print(f"📥 画像をダウンロード中: {image_url}")
                        img_response = requests.get(image_url)

                        if img_response.status_code == 200:
                            with open(output_path, "wb") as f:
                                f.write(img_response.content)

                            print(f"✅ 画像保存: {output_path}")
                            return str(output_path)
                        else:
                            print(
                                f"❌ 画像ダウンロードエラー: {img_response.status_code}"
                            )
                            return None
                    else:
                        print("❌ 生成された画像が見つかりません")
                        return None
                elif status_data.get("status") == "processing":
                    print(f"⏳ 処理中... ({attempt + 1}/{max_attempts})")
                    time.sleep(2)  # 2秒待機
                else:
                    print(f"❌ 予期しないステータス: {status_data.get('status')}")
                    return None
            else:
                print(f"❌ ステータス確認エラー: {response.status_code}")
                return None

            attempt += 1

        print("❌ タイムアウト: 画像生成が完了しませんでした")
        return None

    except Exception as e:
        print(f"❌ 画像生成エラー: {e}")
        return None


def generate_article_images(article_name):
    """記事用の全画像を生成"""
    print(f"🚀 記事用画像生成開始: {article_name}")

    if article_name not in IMAGE_CONFIGS:
        print(f"❌ 設定が見つかりません: {article_name}")
        return

    # Canvaサーバーの確認
    print("🔍 Canva Apps SDKサーバーを確認中...")
    if not check_canva_server():
        print("❌ Canva Apps SDKサーバーが起動していません")
        print("💡 以下のコマンドでサーバーを起動してください:")
        print("   cd note-image-gen && npm start")
        return

    print("✅ Canva Apps SDKサーバーが起動しています")

    # 画像ディレクトリ作成
    image_dir = create_image_directory(article_name)
    print(f"📁 画像ディレクトリ: {image_dir}")

    # 各画像を生成
    generated_images = []
    config = IMAGE_CONFIGS[article_name]

    for image_type, settings in config.items():
        print(f"\n🖼️ {image_type} 画像生成中...")

        output_path = generate_canva_image(
            settings["prompt"], settings["size"], settings["filename"], image_dir
        )

        if output_path:
            generated_images.append(
                {
                    "type": image_type,
                    "path": output_path,
                    "filename": settings["filename"],
                }
            )

    # 生成結果をレポート
    print(f"\n📊 生成完了レポート:")
    print(f"📁 ディレクトリ: {image_dir}")
    print(f"🖼️ 生成画像数: {len(generated_images)}")

    for img in generated_images:
        print(f"  - {img['type']}: {img['filename']}")

    # マークダウン用の画像リンクを生成
    print(f"\n📝 マークダウン用画像リンク:")
    for img in generated_images:
        github_url = f"https://daideguchi.github.io/note-zenn-articles/{img['path']}"
        print(f"![{img['type']}]({github_url})")

    return generated_images


def main():
    """メイン関数"""
    if len(sys.argv) < 2:
        print("使用方法: python generate-canva-images.py <記事名>")
        print("利用可能な記事:")
        for article in IMAGE_CONFIGS.keys():
            print(f"  - {article}")
        return

    article_name = sys.argv[1]
    generate_article_images(article_name)


if __name__ == "__main__":
    main()
