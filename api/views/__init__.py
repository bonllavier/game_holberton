#!/usr/bin/python3
'create an instace of blueprint'
from flask import Blueprint
app_views = Blueprint("my_blueprint", __name__, url_prefix="/api")
from api.views.index import *
from api.views.user import *
