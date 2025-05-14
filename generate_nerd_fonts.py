#!/usr/bin/env python3

import glob
import os
import shutil
import subprocess
import urllib.request
import zipfile

ZIP_URL = "https://github.com/ryanoasis/nerd-fonts/raw/master/FontPatcher.zip"
ZIP_FILE = "FontPatcher.zip"
PATCHER_DIR = "NerdFontPatcher"
FONTS_DIR = "./fonts"


def main():
    if not os.path.isdir(PATCHER_DIR):
        urllib.request.urlretrieve(ZIP_URL, ZIP_FILE)
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(PATCHER_DIR)
        os.remove(ZIP_FILE)

    font_files = [
        f for f in glob.glob(os.path.join(FONTS_DIR, "*.ttf"))
        if "NerdFont" not in os.path.basename(f)
    ]
    if not font_files:
        raise FileNotFoundError("No .ttf files found in the 'fonts' directory")

    for font_path in font_files:
        base_name = os.path.splitext(os.path.basename(font_path))[0]
        print(f"Processing font: {base_name}")

        cmd = [
            "fontforge",
            "-script",
            os.path.join(PATCHER_DIR, "font-patcher"),
            font_path,
            "--complete",
            "--boxdrawing",
            "--no-progressbars",
            "--quiet"
        ]

        subprocess.run(cmd, check=True)


for ttf_file in glob.glob("*.ttf"):
    target_path = os.path.join(FONTS_DIR, os.path.basename(ttf_file))
    shutil.move(ttf_file, target_path)


if __name__ == "__main__":
    main()
