import fontforge

def generate_font(font_type: str, font_weight: int, font_scale: int) -> None:
    font = fontforge.open("NeoSpleen-Regular.ttf")
    font.selection.all()

    # Set font metadata
    font.fontname = f"NeoSpleen-{font_type}"
    font.fullname = f"NeoSpleen {font_type}"
    font.weight = font_type
    font.os2_weight = font_weight
    font.appendSFNTName("English (US)", "SubFamily", font_type)

    # Modify weight of glyphs
    font.changeWeight(font_scale, "LCG", 0, 0, "squish")

    # Generate the new font file
    output_file = f"NeoSpleen-{font_type}.ttf"
    font.generate(output_file)
    print(font)
    font.close()

if __name__ == "__main__":
    generate_font("Bold", 700, 32)
