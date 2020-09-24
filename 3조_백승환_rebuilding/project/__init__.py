from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

mongo = PyMongo(app)

from project.boards import boards_blueprint
from project.members import members_blueprint
# from flask import Blueprint

# main_blueprint = Blueprint('main', __name__, template_folder='templates')

# app.register_blueprint(main_blueprint)
app.register_blueprint(boards_blueprint)
app.register_blueprint(members_blueprint)

from . import routes

