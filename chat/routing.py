from django.urls import re_path
from chat.consumers import ChatConsumer
from chat.notifications import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<conversation_id>\d+)/$', ChatConsumer.as_asgi()),
    re_path(r'ws/notificacoes/$', NotificationConsumer.as_asgi()),
]
