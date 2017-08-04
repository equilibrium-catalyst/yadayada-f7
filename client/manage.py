"""Launches and renders routes for paced's resume page."""

import os

import requests
from flask import (Flask, make_response, redirect, render_template, request,
                   send_from_directory)

# Necessary settings
DEBUG = True

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Standard page redirect."""
    return render_template("pages/home.html")


@app.route('/community/', methods=['GET'])
def about():
    """Standard page redirect."""
    r = requests.get(url='http://localhost:8000/recordings/?format=json')

    for i in r.json():
        print("Line")

    return render_template("pages/community.html", data={'stuff': r.json()})


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Contact forms."""
    return send_from_directory('static/', 'sitemap.xml')


@app.route('/robots.txt')
def robots():
    """Robot file for SEO."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt')


if __name__ == "__main__":
    app.run(debug=DEBUG, host='localhost')
