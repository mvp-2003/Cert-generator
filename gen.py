from flask import Flask, render_template, request
from name_generator.build import generate_certificate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'POST':
        cert_image = request.files['cert_image']
        names = request.files['names']
        directory = request.form['directory']
        generate_certificate(cert_image, names, directory)

    return render_template('home.html')

app.run(port=5000)