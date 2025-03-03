from django.db import models
from loja.models import User  # Importa os utilizadores da loja

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")  # Quem enviou
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")  # Quem recebe
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.content[:50]}"
