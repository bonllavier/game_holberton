#!/usr/bin/python3
'index of status'
from api.views import app_views
from flask import jsonify, abort, request
from models import storage, get_token
from models.user import User


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
    email = dict_parameters("email")
    password = dict_parameters("password")
    api_key = dict_parameters("api_key")

    auth_token = get_token(email, password, api_key);
    if auth_token:
        user = storage.__session.query(User).filter(User.email == email).one_or_none()
        if user:
            ##definir variables en db
        else:
            new_user = User(email, password, api_key, auth_token)
            # set a attributes
            new_user.save()
    else:
        return jsonify({"email": email, "tries": 0, "status": None}), 400

#    state = State(**request.get_json())
#    state.save()
    


@app_views.route('/states/<state_id>', methods=['PUT'])
def put_state_by_id(state_id):
    'retrive an object into a json'
    if not request.get_json():
        abort(400, "Not a JSON")

    state = storage.get("State", state_id)

    if state:
        for key, value in request.get_json().items():
            if key != "id" and key != "created_at" and key != "updated_at":
                setattr(state, key, value)
        state.save()
    else:
        abort(404)

    return jsonify(state.to_dict()), 200




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
