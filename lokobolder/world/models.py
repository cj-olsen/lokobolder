from lokobolder.database import db

CONST_CHUNK_WIDTH = 128

class WorldChunk(db.Model):

    __tablename__ = 'map_tile_chunk'

    id = db.Column(db.Integer, primary_key=True)

    # Our x-offset
    x = db.Column(db.Integer)

    # Our y-offset
    y = db.Column(db.Integer)

    # The map data itself
    data = db.Column(db.String(CONST_CHUNK_WIDTH ** 2))

    
