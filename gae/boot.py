from wsgiref.handlers import CGIHandler
from google.appengine.ext.appstats import recording
import sys, os

root_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(root_dir, 'lib')
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)

from main import app

if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    # use our debug.utils with Jinja2 templates
    import debug.utils
    sys.modules['werkzeug.debug.utils'] = debug.utils

    # don't use inspect.getsourcefile because the imp module is empty
    import inspect
    inspect.getsourcefile = inspect.getfile

    # wrap the application
    from werkzeug import DebuggedApplication
    app = DebuggedApplication(app, evalex=True)

CGIHandler().run(recording.appstats_wsgi_middleware(app))
