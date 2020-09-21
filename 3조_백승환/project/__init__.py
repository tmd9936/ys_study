from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

mongo = PyMongo(app)

from project.boards import boards_blueprint
from project.users import users_blueprint

app.register_blueprint(boards_blueprint)
app.register_blueprint(users_blueprint)


