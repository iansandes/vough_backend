"""
WSGI config for vough_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vough_backend.settings')
os.environ['GITHUB_TOKEN'] = 'token 815fa987802cc0f3ed9982be0d9d30cd76a8a924'

application = get_wsgi_application()
