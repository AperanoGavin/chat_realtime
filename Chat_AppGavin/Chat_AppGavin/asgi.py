"""
ASGI config for Chat_AppGavin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat_AppGavin.settings')

application = get_asgi_application()

import chat.routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter


application = ProtocolTypeRouter(
    {
        'http' : get_asgi_application() ,
        'websocket' : AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )   
        )
    }
)