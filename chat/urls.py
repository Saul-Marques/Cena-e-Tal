from django.urls import path
from chat.views import chat_list_view, iniciar_conversa_produto

urlpatterns = [
    path("", chat_list_view, name="chat_list"),  # Lista de conversas
    path("<int:conversation_id>/", chat_list_view, name="chat_detail"),
    path("produto/<int:produto_id>/iniciar/", iniciar_conversa_produto, name="iniciar_conversa_produto"),
    ]