from django.urls import path
from .views import chat_view, send_private_message

urlpatterns = [
    path("", chat_view, name="chat"),
    path("send_message/", send_private_message, name="send_message"),  # Envio de mensagens privadas
]