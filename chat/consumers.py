import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Conversation, Message
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
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
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")

        if not message:
            logger.warning("Received empty message")
            return

        await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": self.user.primeiro_nome,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
        }))

    @sync_to_async
    def save_message(self, text):
        try:
            conversation = Conversation.objects.get(id=self.conversation_id)
            Message.objects.create(
                conversation=conversation,
                sender=self.user,
                text=text
            )
        except Conversation.DoesNotExist:
            logger.error(f"Conversation with ID {self.conversation_id} not found")
