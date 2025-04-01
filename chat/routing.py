from django.urls import re_path
from chat.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer
from channels.auth import AuthMiddlewareStack
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<conversation_id>\d+)/$', ChatConsumer.as_asgi()),
    ]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})