#!/usr/bin/python3

from flask import Flask, render_template, uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import os

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = sorted(storage.all(State).values(), key=lambda k: k.name)
    st_ct = [[state, sorted(state.cities, key=lambda k: k.name)] for state in states]

    amenities = sorted(storage.all(Amenity).values(), key=lambda k: k.name)
    places = sorted(storage.all(Place).values(), key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    host = os.environ.get("HOST", '0.0.0.0')
    port = os.environ.get("PORT", 5000)
    app.run(host=host, port=port)

