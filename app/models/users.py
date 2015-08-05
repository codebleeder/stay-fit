__author__ = 'sharad'

from app import db


class User(db.Document):
    name = db.StringField(required=True, max_length=100)
    email = db.EmailField(required=True, max_length=100)
    password = db.StringField(required=True, max_length=100)
