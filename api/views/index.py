#!/usr/bin/python3
'index of status'
from api.views import app_views
from flask import jsonify
#from models import storage


@app_views.route("/status")
def status():
    'returns a json of status'
    return jsonify({"status": "OK"})
