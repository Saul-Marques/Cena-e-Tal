from django.test import TestCase
from dashboard.models import Eventos, Comentarios

class EventosModelTests(TestCase):
    def test_create_evento(self):
        evento = Eventos.objects.create(nome="Teste", descricao="Descrição de teste")
        self.assertEqual(str(evento.nome), "Teste")

class ComentariosModelTests(TestCase):
    def test_comentario_str(self):
        evento = Eventos.objects.create(nome="Teste Evento")
        comentario = Comentarios.objects.create(evento=evento, mensagem="Mensagem")
        self.assertEqual(comentario.mensagem, "Mensagem")
