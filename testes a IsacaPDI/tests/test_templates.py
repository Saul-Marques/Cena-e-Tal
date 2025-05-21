from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardTemplateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='12345')

    def test_home_template_contains_periodo_label(self):
        self.client.login(username='tester', password='12345')
        response = self.client.get(reverse('dashboard:home'))
        self.assertContains(response, "Últimos 7 dias")
