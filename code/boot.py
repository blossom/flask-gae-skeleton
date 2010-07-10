from wsgiref.handlers import CGIHandler
from google.appengine.ext.appstats import recording
import sys, os

sys.path.insert(0, os.path.dirname(__file__) + '/lib')

from main import app
CGIHandler().run(recording.appstats_wsgi_middleware(app))
