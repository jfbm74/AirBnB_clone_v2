# !/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """function that prints a greeting"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """function that prints HBNB"""
    return 'HBNB'


@app.route('/c/<string:tag>', strict_slashes=False)
def tagging(tag):
    """function that prints a URL parameter"""
    tag = tag.replace('_', ' ')
    return "C {}".format(tag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
