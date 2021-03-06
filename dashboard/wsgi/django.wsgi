import logging
import os
import sys
import django.core.handlers.wsgi
from django.conf import settings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings'
sys.stdout = sys.stderr

DEBUG = False

application = django.core.handlers.wsgi.WSGIHandler()
