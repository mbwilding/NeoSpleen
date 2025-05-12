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
    """
    Create and save an image with specified text and background colors using a given font.

    Args:
      text_color (str): The color of the text in the image.
      background_color (str): The background color for the image.
      file_path (str): The filename to save the image under.
      font (ImageFont.FreeTypeFont): The font to use for the text.
    """
    # Optionally ensure the output directory exists
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
    # Create a font object for the current file
    font = ImageFont.truetype(ttf_file, FONT_SIZE)
    # Generate output paths
    base_name = os.path.splitext(os.path.basename(ttf_file))[0]
    wob_path = os.path.join("renders", f"{base_name}-WoB.png")
    bow_path = os.path.join("renders", f"{base_name}-BoW.png")
    # Create the images
    create_image("white", "black", wob_path, font)
    create_image("black", "white", bow_path, font)
