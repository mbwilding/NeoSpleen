#!/usr/bin/env python3

"""
This module provides a function to create and save an image with custom text,
and background colors using the Pillow library.
"""
from PIL import Image, ImageDraw, ImageFont

TEXT = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
_-~=+*&#$@%^
/<[{(|)}]>\
`'".,:;!?"""

WIDTH, HEIGHT = 3840, 1350
FONT_PATH = "NeoSpleen.ttf"
FONT_SIZE = 294
FONT = ImageFont.truetype(FONT_PATH, FONT_SIZE)


def create_image(text_color, background_color, file_path):
    """
    Create an save an image with specified text color and background color.

    Args:
    text_color (str): The color of the text in the image.
    background_color (str): The background color of the image.
    file_path (str): The filename to save the image under.
    """
    image = Image.new("RGB", (WIDTH, HEIGHT), background_color)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), TEXT, fill=text_color, font=FONT)
    image.save("fonts/Showcase-" + file_path)


create_image("white", "black", "WoB.png")
create_image("black", "white", "BoW.png")
