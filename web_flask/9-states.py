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


@app.route('/states')
@app.route('/states/<id>')
def states_id(id=None):
    st = storage.all(State)
    cityst = storage.all(City)
    if id is not None:
        for state in st.values():
            if state['id'] == id:
                st = state
    return render_template('9-states.html', states=st, cityst=cityst, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
