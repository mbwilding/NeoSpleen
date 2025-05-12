#!/usr/bin/env python3

import os
import glob
from PIL import Image, ImageDraw, ImageFont

TEXT = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
_-~=+*&#$@%^
/<[{(|)}]>\
`'".,:;!?"""

WIDTH, HEIGHT = 3840, 1290
FONT_SIZE = 294

def create_image(text_color, background_color, file_path, font):
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = Image.new("RGB", (WIDTH, HEIGHT), background_color)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), TEXT, fill=text_color, font=font)
    image.save(file_path)

ttf_files = glob.glob(os.path.join("fonts", "*.ttf"))

for ttf_file in ttf_files:
    if "NerdFont" in os.path.basename(ttf_file):
        continue
    font_ttf = ImageFont.truetype(ttf_file, FONT_SIZE)
    base_name = os.path.splitext(os.path.basename(ttf_file))[0]
    wob_path = os.path.join("renders", f"{base_name}-WoB.png")
    bow_path = os.path.join("renders", f"{base_name}-BoW.png")

    create_image("white", "black", wob_path, font_ttf)
    create_image("black", "white", bow_path, font_ttf)
