from django.shortcuts import render, redirect
from loja.models import User
from chat.models import Conversation

def chat_list_view(request, conversation_id=None):
    """ Página de chat com lista à esquerda e conversa ativa à direita """

    if "user_id" not in request.session:
        return redirect("login")

    try:
        user = User.objects.get(id=request.session["user_id"])
    except User.DoesNotExist:
        return redirect("login")

    # 🔍 DEBUG: Verificar o ID do utilizador logado
    print(f"DEBUG: Utilizador logado -> {user.id} - {user.email}")

    # 🚀 Buscar todas as conversas onde o utilizador está envolvido
    conversations = Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)

    # 🔍 DEBUG: Verificar se conversas foram encontradas
    print(f"DEBUG: Conversas encontradas -> {list(conversations)}")

    active_conversation = None
    messages = []

    if conversation_id:
        active_conversation = conversations.filter(id=conversation_id).first()
        if active_conversation:
            messages = active_conversation.messages.all().order_by("timestamp")

    return render(request, "chat/chat_list.html", {
        "conversations": conversations,
        "active_conversation": active_conversation,
        "messages": messages,
        "user": user
    })
