from django.shortcuts import render, redirect, get_object_or_404
from loja.models import User, Product
from chat.models import Conversation
from django.contrib.auth.decorators import login_required


@login_required
def chat_list_view(request, conversation_id=None):

    user = request.user
    conversations = Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)


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

@login_required
def iniciar_conversa_produto(request, produto_id):
    produto = get_object_or_404(Product, id=produto_id)
    comprador = request.user
    vendedor = produto.user

    if comprador == vendedor:
        return redirect("produto_detail", id=produto.id)

    conversa = Conversation.objects.filter(
        product=produto,
        user1__in=[comprador, vendedor],
        user2__in=[comprador, vendedor]
    ).first()

    if not conversa:
        conversa = Conversation.objects.create(user1=comprador, user2=vendedor, product=produto)
        
    return redirect("chat_detail", conversation_id=conversa.id)

