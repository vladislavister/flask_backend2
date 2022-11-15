from flask import jsonify, request
from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)



CATEGORIES = {
    1: "Food",
    2: "Chemicals"
}


# class Category(db.Model):


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route('/categories/<id>')
def get_category_by_id(id):
    return CATEGORIES[int(id)]


@app.route("/categories", methods=['POST'])
def create_category():
    request_data = request.get_json()
    CATEGORIES[int(request_data['id'])] = request_data['name']
    return "STATUS: OK"


@app.route("/categories/<id>", methods=['DELETE'])
def delete_category(id):
    del CATEGORIES[int(id)]
    return "STATUS: OK"


@app.route("/categories/<id>", methods=['PUT'])
def update_category(id):
    request_data = request.get_json()
    CATEGORIES[int(id)] = request_data['name']
    return "STATUS: OK"