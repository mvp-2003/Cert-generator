import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import io

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_file):
    try:
        font = ImageFont.truetype(font_path, size=84)

        certificate_template = Image.open(certificate_template.stream)

        width, height = certificate_template.size

        if not os.path.exists('Certificates'):
            os.makedirs('Certificates')

        names_file = io.TextIOWrapper(names_file.stream)

        for name in names_file:
            name = name.strip()
            if not name:
                continue

            template_image = certificate_template.copy()
            draw = ImageDraw.Draw(template_image)

            bbox = draw.textbbox((0, 0), name, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = (width - text_width) / 2
            text_y = (height - text_height) / 2

            draw.text((text_x, text_y), name, font=font, fill="black")

            template_image.save(f"Certificates/certificate_{name}.{certificate_template.format.lower()}")

        shutil.make_archive('Certificates', 'zip', 'Certificates')

    except Exception as e:
        print(f"An error occurred: {e}")