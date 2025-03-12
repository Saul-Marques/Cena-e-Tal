from django.contrib import admin
from chat.models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "user1", "user2", "created_at")  # Campos visíveis na lista
    search_fields = ("user1__username", "user2__username")  # Permite pesquisar por usernames
    list_filter = ("created_at",)  # Filtro por data de criação
    ordering = ("-created_at",)  # Ordena pelas conversas mais recentes
    readonly_fields = ("created_at",)  # Impede edição da data

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "sender", "text", "timestamp")  # Campos visíveis na lista
    search_fields = ("sender__username", "text")  # Pesquisa por utilizador ou mensagem
    list_filter = ("timestamp",)  # Filtro por data
    ordering = ("-timestamp",)  # Mensagens mais recentes primeiro
    readonly_fields = ("timestamp",)  # Impede edição da data
