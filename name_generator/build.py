import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import io
import zipfile

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_file):
    try:
        font_size = 96
        font = ImageFont.truetype(font_path, size=font_size)

        certificate_template = Image.open(certificate_template.stream)
        width, height = certificate_template.size

        certificates = []

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

            if text_width > width * 0.8:
                text_x = (width - text_width) * 0.1
            else:
                text_x = (width - text_width) / 2

            text_y = (height - text_height) / 2

            draw.text((text_x, text_y), name, font=font, fill="black")
            output = io.BytesIO()
            template_image.save(output, format=certificate_template.format)
            output.seek(0)
            certificates.append((output, f"certificate_{name}.{certificate_template.format.lower()}"))

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for certificate in certificates:
                output, filename = certificate
                zip_info = zipfile.ZipInfo(filename)
                zip_info.compress_type = zipfile.ZIP_DEFLATED
                zip_file.writestr(zip_info, output.read())

        zip_buffer.seek(0)
        return zip_buffer

    except Exception as e:
        print(f"An error occurred: {e}")
        raise e