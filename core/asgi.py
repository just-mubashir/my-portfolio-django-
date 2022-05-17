"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
# neww impor for channels
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

# new asgi configurationfor channels
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
})

'''
OLD CONFIGURATION

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

'''


'''
CUSTOM ASGI CONFIGURATION FOR CHANNELS

import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
})

'''