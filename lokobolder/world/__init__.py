from flask import Blueprint, jsonify

from .models import WorldChunk

world = Blueprint('world', __name__)

@world.route('/<int:x>/<int:y>', methods=['GET'])
def get_by_coordinates(x, y):
    """Return the world chunk at the given coordinates."""
    # TODO: Query database for the correct chunk, then jsonify and return it.
    smallworld = [["DOOM","Desert","Forest"],
                  ["Town","Lake","Tundra"],
                  ["Shipyards","Boneyards","Gokart Tracks"]]
    return jsonify(smallworld[x][y])
