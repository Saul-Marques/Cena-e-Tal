import json
import logging
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from loja.models import User
from chat.models import Message
from chat.pusher import pusher_client  # Importa a configuração do Pusher

logger = logging.getLogger(__name__)  # Ativa logs para debugging

def chat_view(request):
    users = User.objects.exclude(id=request.session.get("user_id"))  # Exclui o próprio utilizador
    return render(request, "chat.html", {"users": users})

@csrf_exempt
def send_private_message(request):
    """Processa o envio de mensagens privadas entre utilizadores"""
    if request.method == "POST":
        data = json.loads(request.body)
        sender = get_object_or_404(User, id=request.session.get("user_id"))  # ✅ Obtém o utilizador autenticado
        receiver = get_object_or_404(User, id=data.get("receiver_id"))
        message = data.get("message", "")

        # ✅ Guardar a mensagem no banco de dados
        msg = Message.objects.create(sender=sender, receiver=receiver, content=message)

        # ✅ Log para verificar se Django está a processar a mensagem
        logger.info(f"📨 Mensagem enviada: {sender.primeiro_nome} {sender.ultimo_nome} -> {receiver.primeiro_nome} {receiver.ultimo_nome}: {message}")
        print(f"📨 Enviando mensagem para Pusher: {message}")

        # ✅ Enviar para o canal certo
        channel_name = f"private-chat-{receiver.id}"
        event_name = "new-message"

        try:
            pusher_client.trigger(channel_name, event_name, {
                "sender_nome": sender.primeiro_nome,
                "sender_apelido": sender.ultimo_nome,
                "message": message
            })
            logger.info(f"✅ Mensagem enviada com sucesso para Pusher no canal `{channel_name}`")
            print(f"✅ Mensagem enviada com sucesso para Pusher no canal `{channel_name}`")
        except Exception as e:
            logger.error(f"❌ Erro ao enviar para Pusher: {e}")
            print(f"❌ Erro ao enviar para Pusher: {e}")

        return JsonResponse({"success": True})
