#!/usr/bin/python3
""" C_route.py Task 2 """

from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exit):
    storage.close()


@app.route('/cities_by_states')
def cities_x_states():
    st = storage.all(State)
    cityst = storage.all(City)
    return render_template('8-cities_by_states.html', states=st, cityst=cityst)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
