#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """Close session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def all_states():
    """
    List all states on storage
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def search_state(id):
    """
    List a specific state given as parameter in URL
    """
    states = storage.all(State).values()
    for data in states:
        if (id == data.id):
            return render_template("9-states.html", states=data)
        else:
            return render_template("9-states.html", states=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
