#def application(env, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    return [b"uwsgi --http :8002 --wsgi-file wsgi.py"]

"""
WSGI config for labs project.

It exposes the WSGI callable as a module-level variable named   ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labs.settings")

application = get_wsgi_application()