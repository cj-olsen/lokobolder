from flask import Blueprint, jsonify

from .models import WorldChunk

world = Blueprint('world', __name__)

@world.route('/<int:x>/<int:y>', methods=['GET'])
def get_by_coordinates(x, y):

    # Return the world chunk at the given coordinates.

    # To-do: Query database for the correct chunk

    # To-do: Return jsonified chunk data
    return jsonify([])
