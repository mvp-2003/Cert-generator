from flask import Flask, render_template, json, request
from name_generator.build import generate_certificate

app = Flask(__name__)

@app.route('/')
def frontpage():
    if request.method == 'POST':   
        cert_image = request.files['file-upload']
        names = request.files['file-upload-2']

        generate_certificate(cert_image, names)

    return render_template('home.html')

app.run(port=5000)