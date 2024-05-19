import os
import shutil
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(certificate_template, names_file):
    font_path = "arial.ttf"
    font = ImageFont.truetype(font_path, size=84)

    with Image.open(certificate_template) as img:
        width, height = img.size

    if not os.path.exists('Certificates'):
        os.makedirs('Certificates')

    with open(names_file, 'r') as names_list:
        for name in names_list:
            name = name.strip()
            template_image = Image.open(certificate_template)
            draw = ImageDraw.Draw(template_image)
            text_width, text_height = draw.textsize(name, font=font)
            draw.text(((width - text_width) / 2, (height - text_height) / 2), name, font=font, fill="black")
            template_image.save(f"Certificates/certificate_{name}.{certificate_template.split('.')[-1]}")

    shutil.make_archive('Certificates', 'zip', 'Certificates')

    if not os.path.exists(directory):
        os.makedirs(directory)

    shutil.move('Certificates.zip', directory)