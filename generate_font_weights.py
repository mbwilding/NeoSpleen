import fontforge

# Generate bold weight
font = fontforge.open("NeoSpleen-Regular.ttf")
font.selection.all()
font.fontname = "NeoSpleen-Bold"
font.fullname = "NeoSpleen Bold"
font.weight = "Bold"
font.changeWeight(32, "LCG", 0, 0, "squish")
font.generate("NeoSpleen-Bold.ttf")
print(font)
font.close()
