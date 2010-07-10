# coding: UTF-8
from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
    facebook_id = db.StringProperty()

    def photo_url(self):
        return "https://graph.facebook.com/%s/picture" % self.facebook_id
