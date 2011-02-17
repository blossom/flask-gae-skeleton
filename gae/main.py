# coding: UTF-8

import settings

from flask import Flask
app = Flask(__name__)
app.config.from_object('settings')

from flask import g
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import render_template
from flask import abort
from flask import flash
from flask import get_flashed_messages
from flask import json

from decorators import login_required, cache_page

from models import User

from gaeUtils.util import generate_key
from google.appengine.api.labs import taskqueue

@app.before_request
def before_request():
    """
    if the session includes a user_key it will also try to fetch
    the user's object from memcache (or the datastore).
    if this succeeds, the user object is also added to g.
    """
    if 'user_key' in session:
        user = cache.get(session['user_key'])

        if user is None:
            # if the user is not available in memcache we fetch
            # it from the datastore
            user = User.get_by_key_name(session['user_key'])

            if user:
                # add the user object to memcache so we
                # don't need to hit the datastore next time
                cache.set(session['user_key'], user)

        g.user = user
    else:
        g.user = None

@app.route('/')
def index():
    """
    renders the index page template
    """
    return render_template('index.html')
