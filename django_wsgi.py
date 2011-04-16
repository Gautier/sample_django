# first configure the path to add our bundled django, and other libraries
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

# get the django wsgi app
import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()

# then serve it with wsgiref, let cloudfoundry do the rest :)
from wsgiref.simple_server import make_server
PORT = int(os.environ["VCAP_APP_PORT"])
httpd = make_server('', PORT, application)
print "Serving HTTP on port %d..." % PORT

httpd.serve_forever()
