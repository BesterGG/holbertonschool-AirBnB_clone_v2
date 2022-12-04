#!/usr/bin/python3
""" hbnb task1 """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Say Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Say HBNB"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
