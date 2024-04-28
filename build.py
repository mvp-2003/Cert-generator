from PIL import Image, ImageDraw, ImageFont
import os

# Load the certificate template
certificate_template = "Certificate.png"
font_path = "Font.ttf"

# Specify the font and size
font = ImageFont.truetype(font_path, size=84)

# List of names to add to the certificate
names_list = ['Ossama Mehmood', 'Maadeha shaikh ', 'Piyush ', 'Abdul Rehman', 'Shakeel Ahmad']

# Coordinates where the name should be placed
x_position = 560
y_position = 400

# Create the Certificates directory if it doesn't exist
if not os.path.exists('Certificates'):
    os.makedirs('Certificates')

for name in names_list:
    # Load the template image
    template_image = Image.open(certificate_template)
    draw = ImageDraw.Draw(template_image)

    # Add text to the image
    draw.text((x_position, y_position), name, font=font, fill="black")
    
    # Save the new certificate in the Certificates folder
    template_image.save(f"Certificates/certificate_{name}.jpg")