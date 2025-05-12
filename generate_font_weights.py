import fontforge

def generate_font(font_type: str, font_weight: int) -> None:
    font = fontforge.open("fonts/NeoSpleen.ttf")
    font.selection.all()

    # Set font metadata
    font.fontname = f"NeoSpleen-{font_type}"
    font.fullname = f"NeoSpleen {font_type}"
    font.weight = font_type
    font.os2_weight = font_weight
    font.appendSFNTName("English (US)", "SubFamily", font_type)
    font_scale = 1 + (font_weight - 400) * (31 / 300)
    font.changeWeight(font_scale, "LCG", 0, 0, "squish")
    output_file = f"fonts/NeoSpleen-{font_type}.ttf"
    font.generate(output_file)
    print("Type: ", font_type)
    print("Weight: ", font_weight)
    print("Scale: ", font_scale)
    font.close()

if __name__ == "__main__":
    generate_font("Thin", 100)
    generate_font("ExtraLight", 200)
    generate_font("Light", 300)
    generate_font("Regular", 400)
    generate_font("Medium", 500)
    generate_font("SemiBold", 600)
    generate_font("Bold", 700)
    generate_font("ExtraBold", 800)
    generate_font("Black", 900)
