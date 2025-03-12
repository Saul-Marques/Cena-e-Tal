"""
ASGI config for projetoPDI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoPDI.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Mantém o suporte a HTTP
    "websocket": AuthMiddlewareStack(  # Permite WebSockets autenticados
        URLRouter(websocket_urlpatterns)  # Liga as URLs WebSocket
    ),
})
