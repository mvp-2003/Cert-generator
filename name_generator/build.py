from PIL import Image, ImageDraw, ImageFont
import os

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_list):
    font = ImageFont.truetype(font_path, size=84)

    x_position = 400
    y_position = 400

    if not os.path.exists('Certificates'):
        os.makedirs('Certificates')

    for name in names_list:
        template_image = Image.open(certificate_template)
        draw = ImageDraw.Draw(template_image)
        draw.text((x_position, y_position), name, font=font, fill="black")
        template_image.save(f"Certificates/certificate_{name}.jpg")

    names_list.close()