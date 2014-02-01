"""
WSGI config for notes_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import newrelic.agent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_blog.settings.prod")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
application = newrelic.agent.WSGIApplicationWrapper(application)
