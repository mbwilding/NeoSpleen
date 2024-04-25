from PIL import Image, ImageDraw, ImageFont

text = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
_-~=+*&#$@%^
/<[{(|)}]>\
`'".,:;!?"""

width, height = 3840, 1350
font_path = "NeoSpleen.ttf"
font_size = 294
font = ImageFont.truetype(font_path, font_size)


def create_image(background_color, text_color, file_name):
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, fill=text_color, font=font)
    image.save("Showcase-" + file_name)


create_image("black", "white", "WoB.png")
create_image("white", "black", "BoW.png")
