# coding: UTF-8
from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty()
