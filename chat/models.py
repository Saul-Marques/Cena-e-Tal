from django.db import models
from loja.models import User, Product

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations_user2")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2', 'product')

    def __str__(self):
        return f"Chat entre {self.user1.primeiro_nome} e {self.user2.primeiro_nome} sobre {self.product.nome}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.sender.primeiro_nome}: {self.text[:50]}"  # Mostra a data e a mensagem