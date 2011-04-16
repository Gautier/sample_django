import os
import django.core.handlers.wsgi
from wsgiref.simple_server import make_server

# get the django wsgi app
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()

# serve it with wsgiref, let cloudfoundry do the rest :)
PORT = int(os.environ["VCAP_APP_PORT"])
httpd = make_server('', PORT, application)
print "Serving HTTP on port %d..." % PORT

httpd.serve_forever()
