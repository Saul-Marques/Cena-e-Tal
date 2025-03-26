from django.urls import re_path
from chat.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<conversation_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
