import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        self.user = self.scope.get("user")
        if not self.user or not self.user.is_authenticated:
            await self.close()
            return

        self.group_name = f"user_{self.user.id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def nova_mensagem(self, event):
        print("🔔 Notificação recebida no NotificationConsumer!")
        await self.send(text_data=json.dumps({
            "type": "nova_mensagem",
            "message": event["message"],
            "sender": event["sender"],
            "conversation_id": event["conversation_id"],
        }))
