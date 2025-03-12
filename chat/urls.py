from django.urls import path
from chat.views import chat_list_view, chat_view

urlpatterns = [
    path("", chat_list_view, name="chat_list"),  # Lista de conversas
    path("<str:username>/", chat_view, name="chat"),  # Chat privado
]