import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoPDI.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing
from projetoPDI.middleware import WebSocketSessionUserMiddleware

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        WebSocketSessionUserMiddleware(
            URLRouter(chat.routing.websocket_urlpatterns)
        )
    ),
})
