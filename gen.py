from flask import Flask, render_template, request
from name_generator.build import generate_certificate
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'POST':
        cert_image = request.files['cert_image']
        names = request.files['names']

        cert_image_path = os.path.join('uploads', cert_image.filename)
        names_path = os.path.join('uploads', names.filename)
        cert_image.save(cert_image_path)
        names.save(names_path)

        generate_certificate(cert_image_path, names_path, directory)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)