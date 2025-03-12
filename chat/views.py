from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Conversation

@login_required
def chat_list_view(request):
    conversations = Conversation.objects.filter(user1=request.user) | Conversation.objects.filter(user2=request.user)
    return render(request, "chat/chat_list.html", {"conversations": conversations})


@login_required
def chat_view(request, username):
    return render(request, "chat.html", {"other_username": username})
