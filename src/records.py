from datetime import date
from flask import jsonify, request
import uuid

from app import app


class Record:
    def __init__(self, user_id, category_id, money):
        self.user_id = user_id,
        self.category_id = category_id,
        self.creation_date = date.today(),
        self.money = money

    def tojson(self):
        return self.__dict__


RECORDS = {
    '1':Record(1, 1, 250).tojson(),
}


@app.route("/records")
def get_records():
    return RECORDS


@app.route('/records/<id>')
def get_record_by_id(id):
    return RECORDS[id]


@app.route("/records", methods=['POST'])
def create_record():
    r_data = request.get_json()
    rec = Record(r_data['user_id'],
                 r_data['category_id'],
                 r_data['money'])

    RECORDS[str(uuid.uuid4())] = rec.tojson()

    return "STATUS: OK"


@app.route("/records/<id>", methods=['DELETE'])
def delete_record(id):
    del RECORDS[id]
    return "STATUS: OK"


@app.route("/records/<id>", methods=['PUT'])
def update_record(id):
    r_data = request.get_json()

    rec = Record(r_data['user_id'],
                 r_data['category_id'],
                 r_data['money'])

    RECORDS[id] = rec.tojson()

    return "STATUS: OK"