from django.contrib import admin
from chat.models import Conversation, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0  # Impede a criação automática de linhas em branco
    readonly_fields = ("sender", "text", "timestamp")  # Apenas leitura


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "user1", "user2", "created_at")
    search_fields = ("user1__username", "user2__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    inlines = [MessageInline]  # Adiciona mensagens dentro da conversa

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "sender", "text", "timestamp") 
    search_fields = ("sender__username", "text")  
    list_filter = ("timestamp",)  
    ordering = ("-timestamp",) 
    readonly_fields = ("timestamp",)  


