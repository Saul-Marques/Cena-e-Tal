# projetoPDI/asgi.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoPDI.settings')
django.setup()

from channels.auth import AuthMiddleware
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns
from projetoPDI.middleware import WebSocketAuthMiddleware 
import chat.routing 
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': SessionMiddlewareStack(
        AuthMiddleware(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})