c# loja/tests/test_funcionais.py

from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from loja.models import Categoria, Product
from chat.models import Conversation, Message
from asgiref.sync import sync_to_async
from projetoPDI.asgi import application

import pytest
from channels.testing import WebsocketCommunicator
import json

User = get_user_model()

# ---------------------
# TESTES FUNCIONAIS CLÁSSICOS
# ---------------------
class FuncionaisTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.categoria = Categoria.objects.create(
            nome="Tecnologia",
            icon=SimpleUploadedFile("icon.jpg", b"filecontent", content_type="image/jpeg")
        )

        self.vendedor = User.objects.create_user(
            email="vendedor@teste.com",
            primeiro_nome="Vendedor",
            ultimo_nome="Exemplo",
            telemovel="912345678",
            password="vendedor123"
        )

        self.comprador = User.objects.create_user(
            email="comprador@teste.com",
            primeiro_nome="Comprador",
            ultimo_nome="Exemplo",
            telemovel="987654321",
            password="comprador123"
        )

        self.produto = Product.objects.create(
            nome="Projetor HD",
            descricao="Projetor de alta definição",
            preco=120.00,
            categoria=self.categoria,
            user=self.vendedor,
            estado="4",
            tipo_venda="venda"
        )

    def test_homepage_carrega_produto(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Projetor HD")

    def test_upload_produto_requer_login(self):
        response = self.client.get(reverse("upload_product"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_upload_produto_funciona_para_autenticado(self):
        self.client.login(email="vendedor@teste.com", password="vendedor123")
        response = self.client.post(reverse("upload_product"), {
            "nome": "Camera Digital",
            "descricao": "Camera semi-profissional",
            "preco": 80.00,
            "categoria": self.categoria.id,
            "estado": "3",
            "tipo_venda": "venda"
        })
        self.assertIn(response.status_code, [200, 302])

    def test_iniciar_conversa_chat(self):
        self.client.login(email="comprador@teste.com", password="comprador123")
        url = reverse("iniciar_conversa_produto", kwargs={"produto_id": self.produto.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/chat/", response.url)


class ChatMensagensTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.vendedor = User.objects.create_user(
            email="vendedor@teste.com",
            primeiro_nome="Vendedor",
            ultimo_nome="Exemplo",
            telemovel="912345678",
            password="pass123"
        )

        self.comprador = User.objects.create_user(
            email="comprador@teste.com",
            primeiro_nome="Comprador",
            ultimo_nome="Exemplo",
            telemovel="987654321",
            password="pass123"
        )

        self.categoria = Categoria.objects.create(
            nome="Acessórios",
            icon=SimpleUploadedFile("icon.jpg", b"x")
        )

        self.produto = Product.objects.create(
            nome="Relógio Smart",
            descricao="Smartwatch moderno",
            preco=75.00,
            categoria=self.categoria,
            user=self.vendedor,
            estado="4",
            tipo_venda="venda"
        )

        self.conversa = Conversation.objects.create(
            user1=self.comprador,
            user2=self.vendedor,
            product=self.produto
        )

        Message.objects.create(
            conversation=self.conversa,
            sender=self.comprador,
            text="Olá, ainda está disponível?"
        )

    def test_conversa_apresenta_mensagens(self):
        self.client.login(email="comprador@teste.com", password="pass123")
        url = reverse("chat_detail", kwargs={"conversation_id": self.conversa.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Olá, ainda está disponível?")


# ---------------------
# TESTE WEBSOCKET NOTIFICAÇÕES
# ---------------------
@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test_websocket_notificacao_nova_mensagem():
    vendedor = await sync_to_async(User.objects.create_user)(
        email="vendedor@teste.com",
        primeiro_nome="Vendedor",
        ultimo_nome="Teste",
        telemovel="911111111",
        password="pass123"
    )
    comprador = await sync_to_async(User.objects.create_user)(
        email="comprador@teste.com",
        primeiro_nome="Comprador",
        ultimo_nome="Teste",
        telemovel="922222222",
        password="pass123"
    )
    cat = await sync_to_async(Categoria.objects.create)(
        nome="Test",
        icon=SimpleUploadedFile("icon.jpg", b"x")
    )
    produto = await sync_to_async(Product.objects.create)(
        nome="Produto Teste",
        preco=10,
        categoria=cat,
        user=vendedor,
        estado="3",
        tipo_venda="venda"
    )
    conversa = await sync_to_async(Conversation.objects.create)(
        user1=comprador,
        user2=vendedor,
        product=produto
    )

    communicator = WebsocketCommunicator(application, "/ws/notificacoes/")
    communicator.scope["user"] = vendedor
    connected, _ = await communicator.connect()
    assert connected is True

    await communicator.send_json_to({
        "type": "nova_mensagem",
        "message": "Mensagem teste",
        "sender": comprador.email,
        "conversation_id": conversa.id,
    })

    response = await communicator.receive_json_from()
    assert response["type"] == "nova_mensagem"
    assert response["message"] == "Mensagem teste"
    assert response["sender"] == comprador.email
    assert response["conversation_id"] == conversa.id

    await communicator.disconnect()
