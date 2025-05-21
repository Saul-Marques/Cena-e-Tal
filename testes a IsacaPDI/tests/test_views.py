from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='utilizador', password='12345')

    def test_home_view_authenticated(self):
        self.client.login(username='utilizador', password='12345')
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_unauthenticated(self):
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 302)  # deve redirecionar para login
