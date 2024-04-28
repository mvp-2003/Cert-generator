from PIL import Image, ImageDraw, ImageFont

# Load the certificate template
certificate_template = "certificate.png"
font_path = "font.ttf"

# Load the template image
template_image = Image.open(certificate_template)
draw = ImageDraw.Draw(template_image)

# Specify the font and size
font = ImageFont.truetype(font_path, size=24)

# List of names to add to the certificate
names_list = ["Alice"]

# Coordinates where the name should be placed
x_position = 100
y_position = 200

for name in names_list:
    # Add text to the image
    draw.text((x_position, y_position), name, font=font, fill="black")
    
    # Save the new certificate
    template_image.save(f"certificate_{name}.png")
