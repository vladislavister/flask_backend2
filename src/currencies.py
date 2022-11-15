
from flask import jsonify, request
from src import records
from app import app, db, Users, Currencies
from collections import namedtuple
import json

@app.route("/currencies", methods=['GET','POST'])
def create_currency():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            print(request_data)

            c = Currencies(name=request_data['name'], rel_usd=request_data['rel_usd'])
            db.session.add(c)
            db.session.flush()
            db.session.commit()
            print(request_data['name'])
            return "STATUS: OK"
        except:
            db.session.rollback()
            print("Error while adding currency to DB")
    return "Error while adding currency to DB"
