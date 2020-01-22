from flask import Blueprint, jsonify
from lokobolder.database import db

from .models import WorldChunk

world = Blueprint('world', __name__)

@world.route('/<int:x>/<int:y>', methods=['GET'])
def get_by_coordinates(x, y):
    """Return the world chunk at the given coordinates."""
    # TODO: Query database for the correct chunk, then jsonify and return it.
    smallworld = [["DOOM","Desert","Forest"],
                  ["Town","Lake","Tundra"],
                  ["Shipyards","Boneyards","Gokart Tracks"]]
    db.create_all()
    db.session.add(WorldChunk(x=0,y=0,data="some useless rocks"))
    return jsonify(WorldChunk.query.filter_by(x=x,y=y).first().data)
