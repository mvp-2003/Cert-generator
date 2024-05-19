import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import io

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_file):
    font = ImageFont.truetype(font_path, size=84)

    certificate_template = Image.open(certificate_template.stream)

    width, height = certificate_template.size

    if not os.path.exists('Certificates'):
        os.makedirs('Certificates')
        
    names_file = io.TextIOWrapper(names_file.stream)

    for name in names_file:
        name = name.strip()
        template_image = certificate_template.copy()
        draw = ImageDraw.Draw(template_image)
        text_width, text_height = draw.textsize(name, font=font)
        draw.text(((width - text_width) / 2, (height - text_height) / 2), name, font=font, fill="black")
        template_image.save(f"Certificates/certificate_{name}.{certificate_template.format}")

    shutil.make_archive('Certificates', 'zip', 'Certificates')