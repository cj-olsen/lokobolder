from flask import Flask

from .database import db

from .main import main as main_blueprint
from .world import world as world_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)

app.register_blueprint(main_blueprint)
app.register_blueprint(world_blueprint, url_prefix='/api/v1/world/')
