"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/yukif9729/djangogirls'

if path not in sys.path:
    sys.path.append(path)
"""
sys.path.insert(0, path)
"""
os.chdir(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
"""
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
"""
import django
django.setup()
#
## then:

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
