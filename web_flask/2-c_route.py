#!/usr/bin/python3
""" C_route.py Task 2 """

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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Return URL Route with variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
