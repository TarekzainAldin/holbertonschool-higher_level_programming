#!/usr/bin/python3
"""Basic flask application that renders a HTML template"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='/home/tarek/holbertonschool-higher_level_programming-12/python-server_side_rendering/templates ')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)