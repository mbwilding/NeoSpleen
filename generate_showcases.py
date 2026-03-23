#!/usr/bin/env python3

import base64
import glob
import os
import shutil

FONT_SIZE = 150
LINE_HEIGHT = FONT_SIZE * 1.2
TEXT_LINES = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "_-~=+*&#$@%^",
    "/<[{(|)}]>\\",
    "`'\".,:;!?",
]


def create_svg(text_color, file_path, ttf_path, font_family):
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(ttf_path, "rb") as f:
        font_b64 = base64.b64encode(f.read()).decode("ascii")

    num_lines = len(TEXT_LINES)
    width = 2500
    height = int(2 + num_lines * LINE_HEIGHT)

    text_elements = []
    for i, line in enumerate(TEXT_LINES):
        y = int(LINE_HEIGHT + (i + 1) * LINE_HEIGHT)
        # Escape XML special characters
        safe_line = (
            line.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
        text_elements.append(
            f'  <text x="0" y="{y}" fill="{text_color}">{safe_line}</text>'
        )

    text_block = "\n".join(text_elements)

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <defs>
    <style>
      @font-face {{
        font-family: '{font_family}';
        src: url('data:font/truetype;base64,{font_b64}') format('truetype');
      }}
      text {{
        font-family: '{font_family}', monospace;
        font-size: {FONT_SIZE}px;
        white-space: pre;
      }}
    </style>
  </defs>
{text_block}
</svg>
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg)


def main():
    shutil.rmtree("assets", ignore_errors=True)
    os.makedirs("assets", exist_ok=True)
    ttf_files = glob.glob(os.path.join("fonts", "*.ttf"))
    for ttf_file in ttf_files:
        if "NerdFont" in os.path.basename(ttf_file):
            continue
        base_name = os.path.splitext(os.path.basename(ttf_file))[0]
        # Use a unique family name per file to avoid browser caching collisions
        font_family = base_name
        dark_path = os.path.join("assets", f"{base_name}-Dark.svg")
        light_path = os.path.join("assets", f"{base_name}-Light.svg")

        create_svg("white", dark_path, ttf_file, font_family)
        create_svg("black", light_path, ttf_file, font_family)


if __name__ == "__main__":
    main()
