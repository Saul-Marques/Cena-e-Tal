from django.urls import path
from chat.views import chat_list_view

urlpatterns = [
    path("", chat_list_view, name="chat_list"),  # Lista de conversas
    path("<int:conversation_id>/", chat_list_view, name="chat_detail"),
    ]