from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from src import records
from app import app, db, Users
from collections import namedtuple
import json

USERS = {
    1: "Johny Bravo",
    2: "Peter Griffin"
}


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route('/users/<id>')
def get_user_by_id(id):
    USER_RECORDS = []
    for key in records.RECORDS:
        recordJSON = records.RECORDS[key]
        if recordJSON['user_id'] == (int(id),):
            USER_RECORDS.append(recordJSON)

    return jsonify({"user": USERS[int(id)],
                    "users_records": USER_RECORDS})


@app.route("/users", methods=['POST'])
def create_user():
    try:
        request_data = request.get_json()
        print(request_data)

        u = Users(name=request.form['name'], currency_id=request.form['currency'])
        db.session.add(u)
        db.session.flush()
        return "STATUS: OK"
    except:
        db.session.rollback()
        print("Error while adding user to DB")
    return "Error while adding user to DB"


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    del USERS[int(id)]
    return "STATUS: OK"


@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    request_data = request.get_json()
    USERS[int(id)] = request_data['name']
    return "STATUS: OK"

