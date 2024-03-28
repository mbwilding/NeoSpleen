from PIL import Image, ImageDraw, ImageFont

width, height = 3840, 1350
image = Image.new("RGB", (width, height), "black")

font_path = "NeoSpleen.ttf"
font_size = 294
font = ImageFont.truetype(font_path, font_size)

draw = ImageDraw.Draw(image)
text = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
_-~=+*&#$@%^
/<[{(|)}]>\
`'".,:;!?"""

draw.text((0, 0), text, fill="white", font=font)

image.save("Showcase.png")
