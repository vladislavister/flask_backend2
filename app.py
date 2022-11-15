from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'), default='1')

    def __repr__(self):
        return f"<users {self.id}>"


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<categories {self.id}>"


class Currencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rel_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<currencies {self.id}>"


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<records {self.id}>"

@app.route('/')
def welcome_page():  # put application's code here
    return render_template("index.html")

from src import users
from src import categories
from src import records
from src import currencies