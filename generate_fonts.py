#!/usr/bin/env python3

import os
import shutil
import sys

import fontforge


def generate_font(font_type: str, font_weight: int, ext: str) -> None:
    font = fontforge.open("NeoSpleen.sfd")

    font.selection.all()

    font.fontname = f"NeoSpleen-{font_type}"
    font.fullname = f"NeoSpleen {font_type}"
    font.weight = font_type
    font.os2_weight = font_weight
    font.appendSFNTName("English (US)", "SubFamily", font_type)
    output_file = f"fonts/NeoSpleen-{font_type}.{ext}"

    font_scale = 1 + (font_weight - 400) * (31 / 300)
    if font_scale != 1.0:
        font.changeWeight(font_scale, "LCG", 0, 0, "squish")

    font.removeOverlap()
    font.correctDirection()

    for glyph in font.glyphs():
        glyph.simplify()
        glyph.round()

    if ext.lower() in ("ttf", "ttc"):
        font.autoHint()
        font.autoInstr()

    font.generate(output_file)
    print(f"Generated {output_file}:")
    print("  Type:", font_type)
    print("  Weight:", font_weight)
    print("  Scale:", font_scale)
    font.close()


def main():
    formats = sys.argv[1:]
    if not formats:
        formats = ["ttf", "woff2"]

    shutil.rmtree("fonts", ignore_errors=True)
    os.makedirs("fonts", exist_ok=True)

    font_weights = [
        # ("Thin", 100),
        # ("ExtraLight", 200),
        # ("Light", 300),
        ("Regular", 400),
        ("Medium", 500),
        # ("SemiBold", 600),
        ("Bold", 700),
        # ("ExtraBold", 800),
        # ("Black", 900)
    ]

    for ext in formats:
        for font_type, font_weight in font_weights:
            generate_font(font_type, font_weight, ext)


if __name__ == "__main__":
    main()
