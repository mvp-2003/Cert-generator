from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template('home.html')

app.run(port=5000)