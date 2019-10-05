#!/usr/bin/python3
"""api file with the api flask instance"""
from flask import Flask, jsonify, make_response
from models import storage
from api.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def shutdown_session(exception=None):
    "close the session"
    storage.close()


@app.errorhandler(404)
def not_found(e):
    'error handling'
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=5001, threaded=True)
