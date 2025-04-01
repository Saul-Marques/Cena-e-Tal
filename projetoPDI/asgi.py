# asgi.py
import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns
from loja.middleware import CustomAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoPDI.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": CustomAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    ),
})
