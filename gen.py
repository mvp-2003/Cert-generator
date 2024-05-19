from flask import Flask, render_template, request
from name_generator.build import generate_certificate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'POST':
        cert_image = request.files['cert_image']
        names = request.files['names']

        cert_image.save(cert_image.filename)
        names.save(names.filename)

        generate_certificate(cert_image.filename, names.filename)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)