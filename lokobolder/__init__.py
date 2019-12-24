import os

from flask import Flask

from .database import db

from .main import main as main_blueprint
from .world import world as world_blueprint

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Test settings
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # Initialize the database
    db.init_app(app)

    # Register our blueprints.
    app.register_blueprint(main_blueprint)
    app.register_blueprint(world_blueprint, url_prefix='/api/v1/world/')

    return app
