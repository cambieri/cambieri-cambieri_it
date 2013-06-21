import os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'cambieri_it.settings.stage'
application = django.core.handlers.wsgi.WSGIHandler()
