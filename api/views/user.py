#!/usr/bin/python3
'index of status'
from api.views import app_views
from flask import jsonify, abort, request
from models.get_token import get_token
from models.user import User
#from models import storage
import models

storage = models.storage

@app_views.route('/user/', methods=['POST'])
def post_user():
    'retrive an object into a json'
    if not request.get_json():
        abort(400, "Not a JSON")
    if not request.get_json().get("email"):
        abort(400, "Missing email")
    if not request.get_json().get("password"):
        abort(400, "Missing password")
    if not request.get_json().get("api_key"):
        abort(400, "Missing api key")

    dict_parameters = request.get_json()
    email = dict_parameters.get("email")
    password = dict_parameters.get("password")
    api_key = dict_parameters.get("api_key")

    auth_token = get_token(email, password, api_key);
    if auth_token:
        user = storage.check_user(email)
        if user:
            pass
            ##definir variables en db
        else:
            new_user = User(email, password, api_key, auth_token)
            new_user.get_id_proyect(password)
            new_user.save()

            return jsonify({"user": "created"}), 200
    else:
        return jsonify({"email": email, "tries": 0, "status": None}), 400

@app_views.route('/points/<user_id>', methods=['PUT'])
def put_state_by_id(user_id):
    'retrive an object into a json'
    if not request.get_json():
        abort(400, "Not a JSON")

    user = storage.get(user_id)

    if user:
        for key, value in request.get_json().items():
            if key == "points" or key == "turns_done":
                setattr(user, key, value)
        user.save()
    else:
        abort(404)

    return jsonify({"status": "success"}), 200


@app_views.route("/user")
def user():
    """retrive an object into a json"""
    return jsonify({"nombre":"juan"})


@app_views.route("states/<state_id>")
def get_state_by_id(state_id):
    'retrive an object into a json'

    state = storage.get("State", state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('states/<state_id>', methods=['DELETE'])
def delete_state_by_id(state_id):
    'retrive an object into a json'

    state = storage.get("State", state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)
