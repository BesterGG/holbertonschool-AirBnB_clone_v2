#!/usr/bin/python3
""" Module 3-hbnb_route """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(escape(text.replace("_", " ")))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
