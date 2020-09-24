from flask import Blueprint

from flask import render_template, request, url_for
from flask import url_for, redirect, flash, session, abort

from flask_pymongo import ObjectId

from project.commons import constant as const
from project.commons.decorates import login_required

from project import mongo

boards_blueprint = Blueprint(
            'board', 
            __name__, 
            template_folder='templates',
            url_prefix="/board")

from . import routes