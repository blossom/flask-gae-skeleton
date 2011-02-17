# coding: UTF-8

from flask import g
from flask import redirect
from flask import url_for

from functools import wraps

from werkzeug.contrib.cache import GAEMemcachedCache
cache = GAEMemcachedCache()

def login_required(f):
    """
    redirects to the index page if the user has no session
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def cache_page(timeout=5 * 60, key='view/%s'):
    """
    caches a full page in memcache, takes a timeout in seconds
    which specifies how long the cache should be valid.
    also allows a formatstring to be used as memcache key prefix.

    source:
    http://flask.pocoo.org/docs/patterns/viewdecorators/#caching-decorator
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator
