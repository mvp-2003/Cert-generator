from PIL import Image, ImageDraw, ImageFont
import os, shutil

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_file, directory):
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
            template_image.save(f"Certificates/certificate_{name}.jpg")

    shutil.make_archive('Certificates', 'zip', 'Certificates')
    shutil.move('Certificates.zip', directory)