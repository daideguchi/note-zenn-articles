#!/usr/bin/env python3
"""
MarkdownファイルをHTMLに変換してGitHub Pagesで表示できるようにするスクリプト
"""

import sys
import os
from pathlib import Path
import markdown
import re


def create_html_from_markdown(markdown_file):
    """MarkdownファイルをHTMLに変換"""

    # Markdownファイルを読み込み
    with open(markdown_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # MarkdownをHTMLに変換
    html_content = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    # HTMLテンプレートを作成
    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI思考タグ監視記事</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
        }}
        h3 {{
            color: #7f8c8d;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Monaco', 'Menlo', monospace;
        }}
        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .copy-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            z-index: 1000;
        }}
        .copy-button:hover {{
            background: #2980b9;
        }}
        .success {{
            background: #27ae60 !important;
        }}
    </style>
</head>
<body>
    <button class="copy-button" onclick="copyMarkdown()">📋 マークダウンをコピー</button>
    <div class="container">
        {html_content}
    </div>
    
    <script>
        function copyMarkdown() {{
            const button = document.querySelector('.copy-button');
            const originalText = button.textContent;
            
            // マークダウンコンテンツを取得（HTMLから逆変換）
            const container = document.querySelector('.container');
            const markdownContent = `{md_content.replace('`', '\\`').replace('\\', '\\\\')}`;
            
            navigator.clipboard.writeText(markdownContent).then(function() {{
                button.textContent = '✅ コピー完了！';
                button.classList.add('success');
                
                setTimeout(function() {{
                    button.textContent = originalText;
                    button.classList.remove('success');
                }}, 2000);
            }});
        }}
    </script>
</body>
</html>"""

    return html_template


def main():
    """メイン関数"""
    if len(sys.argv) < 2:
        print("使用方法: python markdown-to-html.py <markdownファイル>")
        return

    markdown_file = sys.argv[1]

    if not os.path.exists(markdown_file):
        print(f"❌ ファイルが見つかりません: {markdown_file}")
        return

    # HTMLファイル名を生成
    html_file = markdown_file.replace(".md", ".html")

    # HTMLを生成
    html_content = create_html_from_markdown(markdown_file)

    # HTMLファイルを保存
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTMLファイルを生成しました: {html_file}")
    print(
        f"🌐 GitHub Pages URL: https://daideguchi.github.io/note-zenn-articles/published/{os.path.basename(html_file)}"
    )


if __name__ == "__main__":
    main()
