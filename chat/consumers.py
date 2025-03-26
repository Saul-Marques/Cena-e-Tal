import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from chat.models import Conversation, Message
from loja.models import User
from asgiref.sync import sync_to_async
import logging
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("User model being used:", get_user_model())
        print("User in scope:", self.scope.get("user"))

        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f"chat_{self.conversation_id}"
        self.user = self.scope["user"]

        if not self.user.is_authenticated:
            logger.debug("WebSocket rejected - user not authenticated")
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        logger.debug(f"WebSocket accepted for user {self.user.email} in room {self.room_group_name}")

    async def disconnect(self, close_code):
        # Verifica se `room_group_name` existe antes de tentar remover do grupo
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        # Guarda a mensagem na BD
        await self.save_message(message)

        # Envia para o grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": self.user.primeiro_nome,
            }
        )

    async def chat_message(self, event):
        # Enviar mensagem para o front-end
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
        }))
    def get_or_create_conversation(self):
        other_user = User.objects.get(username=self.other_username)
        conversation, created = Conversation.objects.get_or_create(
            user1=min(self.user, other_user, key=lambda u: u.id),
            user2=max(self.user, other_user, key=lambda u: u.id),
        )
        return conversation
    @sync_to_async
    def save_message(self, text):
        conversation = Conversation.objects.get(id=self.conversation_id)
        Message.objects.create(
            conversation=conversation,
            sender=self.user,
            text=text
        )
