from flask import Flask, render_template, request, send_file
from name_generator.build import generate_certificate
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'POST':
        if 'cert_image' not in request.files or 'names' not in request.files:
            return "No file part", 400

        cert_image = request.files['cert_image']
        names = request.files['names']

        if cert_image.filename == '' or names.filename == '':
            return "No selected file", 400

        try:
            zip_buffer = generate_certificate(cert_image, names)
            return send_file(
                zip_buffer,
                as_attachment=True,
                download_name='Certificates.zip',
                mimetype='application/zip'
            )
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template('home.html')