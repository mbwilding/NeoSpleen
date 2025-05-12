#!/usr/bin/env python3

import os
import subprocess
import urllib.request
import zipfile
import glob
import shutil

zip_url = "https://github.com/ryanoasis/nerd-fonts/raw/master/FontPatcher.zip"
zip_file = "FontPatcher.zip"
patcher_dir = "NerdFontPatcher"
fonts_dir = "./fonts"

if not os.path.exists(zip_file):
    print("Downloading FontPatcher.zip...")
    urllib.request.urlretrieve(zip_url, zip_file)
    print("Download complete")
else:
    print("FontPatcher.zip already exists, skipping download")

if not os.path.isdir(patcher_dir):
    print("Unzipping FontPatcher.zip into", patcher_dir)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(patcher_dir)
    print("Unzip complete.")
else:
    print(f"{patcher_dir} already exists, skipping unzip")

font_files = [
    f for f in glob.glob(os.path.join(fonts_dir, "*.ttf"))
    if "NerdFont" not in os.path.basename(f)
]
if not font_files:
    print("No .ttf font files found in the ./fonts folder")
else:
    for font_path in font_files:
        base_name = os.path.splitext(os.path.basename(font_path))[0]
        print(f"Processing font: {base_name}")

        cmd = [
            "fontforge",
            "-script",
            os.path.join(patcher_dir, "font-patcher"),
            font_path,
            "--complete",
            "--boxdrawing",
            "--no-progressbars",
            "--quiet"
        ]

        subprocess.run(cmd, check=True)

    for ttf_file in glob.glob("*.ttf"):
        target_path = os.path.join(fonts_dir, os.path.basename(ttf_file))
        print(f"Moving {ttf_file} to {target_path}")
        shutil.move(ttf_file, target_path)
