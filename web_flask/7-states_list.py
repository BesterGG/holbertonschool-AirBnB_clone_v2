#!/usr/bin/python3
""" C_route.py Task 2 """

from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exit):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
