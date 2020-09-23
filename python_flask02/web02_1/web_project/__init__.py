from flask import Flask
from flask import request, render_template
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from flask import abort, redirect, url_for, flash
from flask import session
import time
import math

app = Flask(__name__)
# myweb 데이터베이스명 생성, 있으면 그냥 연결
app.config["MONGO_URI"] = "mongodb://localhost:27017/myweb"

# 30분 동안 session 유지되는 환경설정(30분간 아무반응이 없으면 session값은 사라짐)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
# flash를 사용하게되면 SECRET_KEY를 사용해야한다.
app.config["SECRET_KEY"] = "some_key"

mongo = PyMongo(app)

# web프로젝트에 각 모듈들을 포함시킴
from .common import login_required
from .filter import datetime_format
from . import board
from . import member