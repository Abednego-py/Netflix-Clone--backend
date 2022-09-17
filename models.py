import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column, String, Integer
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)


class UserEmail(db.Model):
    __tablename__ = 'userEmail'

    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String, nullable=False, unique=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)