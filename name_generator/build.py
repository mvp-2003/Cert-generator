from PIL import Image, ImageDraw, ImageFont
import os, shutil

font_path = "name_generator/Font.ttf"

def generate_certificate(certificate_template, names_file, directory):
    font = ImageFont.truetype(font_path, size=84)

    with Image.open(certificate_template) as img:
        width, height = img.size

    if not os.path.exists('Certificates'):
        os.makedirs('Certificates')

    names_list = open(names_file, 'r')

    for name in names_list:
        template_image = Image.open(certificate_template)
        draw = ImageDraw.Draw(template_image)
        draw.text((width, height), name, font=font, fill="black")
        template_image.save(f"Certificates/certificate_{name}.jpg")

    names_list.close()

    shutil.make_archive('Certificates', 'zip', 'Certificates')
    shutil.move('Certificates.zip', directory)