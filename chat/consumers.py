import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Conversation, Message 
from asgiref.sync import sync_to_async
from django.utils import timezone

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        except KeyError:
            logger.error("conversation_id not found in URL route kwargs.")
            await self.close()
            return

        self.room_group_name = f"chat_{self.conversation_id}"
        self.user = self.scope.get("user")

        if not self.user or not self.user.is_authenticated:
            logger.warning(f"WebSocket rejected for {self.scope['client']} - user not authenticated or not found in scope.")
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        logger.info(f"WebSocket accepted for user {self.user.email} (ID: {self.user.id}) in room {self.room_group_name}")

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected for user {getattr(self.user, 'email', 'N/A')} from room {getattr(self, 'room_group_name', 'N/A')} with code {close_code}")
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_text = data.get("message")

            if not message_text:
                logger.warning(f"Received empty message from user {self.user.id}")
                return

            saved_message = await self.save_message(message_text)

            if saved_message:
                formatted_time = timezone.localtime(saved_message.timestamp).strftime('%H:%M')

                message_data = {
                    "type": "chat_message", 
                    "message": saved_message.text,
                    "username": self.user.primeiro_nome, 
                    "user_id": self.user.id, 
                    "time": formatted_time,
                }

                await self.channel_layer.group_send(
                    self.room_group_name,
                    message_data
                )
                logger.debug(f"Sent message from user {self.user.id} to group {self.room_group_name}")
                receiver = await self.get_receiver_user(saved_message)

                if receiver.id != self.user.id:
                    await self.channel_layer.group_send(
                        f"user_{receiver.id}",
                        {
                            "type": "nova_mensagem",
                            "message": saved_message.text,
                            "sender": self.user.primeiro_nome,
                            "conversation_id": saved_message.conversation.id,
                        }
                    )

            else:
                 logger.error(f"Failed to save message for user {self.user.id} in conversation {self.conversation_id}")

        except json.JSONDecodeError:
            logger.error(f"Failed to decode JSON from user {getattr(self.user, 'id', 'N/A')}: {text_data}")
        except Exception as e:
             logger.exception(f"Error in receive method for user {getattr(self.user, 'id', 'N/A')}: {e}")


    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        user_id = event["user_id"]
        time = event["time"] 

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "user_id": user_id, 
            "time": time,       
        }))
        logger.debug(f"Sent message event to client {self.channel_name}")

    async def nova_mensagem(self, event):
        await self.send(text_data=json.dumps({
            "type": "nova_mensagem",
            "message": event["message"],
            "sender": event["sender"],
            "conversation_id": event["conversation_id"],
        }))
    
    @sync_to_async
    def get_receiver_user(self, message_obj):
        conv = message_obj.conversation
        return conv.user1 if conv.user2 == self.user else conv.user2


    @sync_to_async
    def save_message(self, text):
        """Saves a message to the database and returns the Message object."""
        try:
            conversation = Conversation.objects.filter(id=self.conversation_id).first()
            if conversation and self.user.is_authenticated:
                 message_obj = Message.objects.create(
                    conversation=conversation,
                    sender=self.user,
                    text=text
                 )
                 logger.info(f"Message saved (ID: {message_obj.id}) for user {self.user.id} in conversation {self.conversation_id}")
                 return message_obj 
            else:
                if not conversation:
                    logger.error(f"Conversation with ID {self.conversation_id} not found during save attempt.")
                if not self.user.is_authenticated:
                     logger.error(f"User not authenticated during save attempt (User ID: {getattr(self.user, 'id', 'N/A')}).")
                return None
        except Exception as e:
            logger.exception(f"Database error saving message for user {self.user.id} in conversation {self.conversation_id}: {e}")
            return None