import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from chat.models import Conversation, Message
from loja.models import User
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f'chat_{self.conversation_id}'
        
        # Get the user from the scope
        self.user = self.scope["user"]
        
        # Check if the user is authenticated
        if self.user.is_authenticated:
            # Join the room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            
            # Accept the connection
            await self.accept()
            
            # Debug log - only access email if user is authenticated
            logger.debug(f"WebSocket accepted for user {self.user.email} in room {self.room_group_name}")
        else:
            # Debug log for anonymous users
            logger.debug(f"WebSocket rejected - user not authenticated")
            
            # Reject the connection
            await self.close()
        logger.debug(f"URL route: {self.scope['url_route']}")
        
        self.conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        logger.debug(f"Conversation ID from URL: {self.conversation_id}")
        
        self.room_group_name = f"chat_{self.conversation_id}"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        logger.debug(f"WebSocket accepted for user {self.user.email} in room {self.room_group_name}")
        await self.accept()

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

        # Enviar mensagem para o grupo WebSocket
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": self.user.primeiro_nome,  # Usar o nome do utilizador autenticado
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

    def save_message(self, text):
        message = Message.objects.create(
            conversation=self.conversation,
            sender=self.user,
            text=text
        )
        return message
