import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from chat.models import Conversation, Message
from asgiref.sync import sync_to_async

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.other_username = self.scope["url_route"]["kwargs"]["username"]

        if not self.user.is_authenticated:
            await self.close()
            return

        # Obter ou criar a conversa
        self.conversation = await sync_to_async(self.get_or_create_conversation)()
        self.room_group_name = f"chat_{self.conversation.id}"

        # Adicionar ao grupo da conversa
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data["message"]

        if not self.user.is_authenticated:
            return

        # Salvar a mensagem no banco de dados
        message = await sync_to_async(self.save_message)(message_text)

        # Enviar mensagem para o grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message.text,
                "username": message.sender.username,
                "timestamp": str(message.timestamp)
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    def get_or_create_conversation(self):
        other_user = User.objects.get(username=self.other_username)
        conversation, created = Conversation.objects.get_or_create(
            user1=min(self.user, other_user, key=lambda u: u.id),
            user2=max(self.user, other_user, key=lambda u: u.id),
        )
        return conversation

    def save_message(self, text):
        message = Message.objects.create(
            conversation=self.conversation,
            sender=self.user,
            text=text
        )
        return message
