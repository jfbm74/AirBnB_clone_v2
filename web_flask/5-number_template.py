#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """function that prints a greeting"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """function that prints HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def tagging(text):
    """function that prints a URL parameter"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def any_route(text='is cool'):
    """function that prints a URL parameter by default"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """function that prints a number given as URL parameter"""
    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """function that prints a number into template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
