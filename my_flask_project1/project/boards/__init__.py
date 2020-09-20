from flask import Blueprint
boards_blueprint = Blueprint(
            'boards', 
            __name__, 
            template_folder='templates')

from . import routes